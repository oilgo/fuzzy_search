import os
import pandas as pd
import numpy as np
from fastapi import HTTPException, status
from difflib import SequenceMatcher
from core.logs.schemas import ErrorRequest
from .schemas import SearchRequest


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


async def get_similar_values(
    value: SearchRequest
):
    """ Method to return similar values
    """

    try:

        df = pd.read_csv(
            filepath_or_buffer = f"./apps/database/{ value.file_name }")

    except Exception as e:

        detail = f"{value.file_name} not found."

        error = ErrorRequest(
            error_code = 404, 
            error_description = detail, 
            user_ip = "127.0.0.1", 
            error_source = os.getcwd() + '\\' + os.path.basename(__file__))

        await error.write_log_errors()

        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = detail)

    models = list(df.ModelName)
    length = len(models)

    if length == 0:

        detail = f"No data found in { value.file_name }"

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