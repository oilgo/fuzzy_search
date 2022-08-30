import os
import pandas as pd
import numpy as np
from fastapi import HTTPException, status
from difflib import SequenceMatcher
from core.logs.schemas import ErrorRequest
from .schemas import SearchRequest
from core.database import engine


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


async def _get_values(
    value: SearchRequest
):
    if value.type == "csv":

        df = await read_from_csv(
            value = value.name)

    elif value.type == "database":

        df = await read_from_db(
            value = value.name)
    else:

        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Invalid format.")

    return await get_similar_values(
        value = value, 
        df = df)


async def get_similar_values(
    value: SearchRequest, 
    df: pd.DataFrame
):
    """ Method to return similar values
    """

    models = list(df.ModelName)
    length = len(models)

    if length == 0:

        detail = f"No data found in { value.name }"

        error = ErrorRequest(
            error_code = 404, 
            error_description = detail, 
            user_ip = "127.0.0.1", 
            error_source = os.getcwd() + '\\' + os.path.basename(__file__))

        await error.write_log_errors()

        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = detail)

    similarity_list = [0] * length

    for i in range(length):
        similarity_list[i] = round(similar(value.new_model, models[i]) * 100, value.round)

    output_df = pd.DataFrame(
        data = np.asarray(similarity_list), 
        index = models, 
        columns = ["new_model"])

    output = output_df.loc[output_df["new_model"] >= value.percent].sort_values("new_model", ascending=False).head(value.limit)

    if output.empty:

        detail = "No data found for your request."

        error = ErrorRequest(
            error_code = 404, 
            error_description = detail, 
            user_ip = "127.0.0.1", 
            error_source = os.getcwd() + '\\' + os.path.basename(__file__))

        await error.write_log_errors()

        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = detail)

    return {
        "similar_values": output.to_dict()["new_model"]
    }


async def read_from_db(
    value: str
):
    try:

        df = pd.read_sql_query(
            sql = f"SELECT \"ModelName\" from public.\"{ value }\";", 
            con = engine)

        return df

    except:

        await no_file(
            value = value)


async def read_from_csv(
    value: str
):
    try:

        df = pd.read_csv(
            filepath_or_buffer = f"./apps/database/{ value }.csv")
        return df

    except:

        await no_file(
            value = value)
    

async def no_file(
    value: str
):
    
    detail = f"{ value } not found."

    error = ErrorRequest(
        error_code = 404, 
        error_description = detail, 
        user_ip = "127.0.0.1", 
        error_source = os.getcwd() + '\\' + os.path.basename(__file__))

    await error.write_log_errors()

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND, 
        detail = detail)