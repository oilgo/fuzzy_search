import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from .validations import SearchRequest
from fastapi import HTTPException, status
from core.logs.schemas import ErrorRequest
import os

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

async def get_similar_values(value: SearchRequest):
    '''returns similar values from the database'''
    try:
        df = pd.read_csv(f'./apps/database/{value.file_name}')
    except:
        detail = f"file {value.file_name} not found"
        error = ErrorRequest(404, detail, '127.0.0.1', os.getcwd() + '\\' + os.path.basename(__file__))
        await error.write_log_errors()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    models = list(df.ModelName)
    length = len(models)
    if length == 0:
        detail = f"no data found in {value.file_name}"
        error = ErrorRequest(404, detail, '127.0.0.1', os.getcwd() + '\\' + os.path.basename(__file__))
        await error.write_log_errors()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    similarity_list = [0] * length
    for i in range(length):
        similarity_list[i] = round(similar(value.new_model, models[i]) * 100, value.round)
    output_df = pd.DataFrame(np.asarray(similarity_list), index=models, columns=['new_model'])
    output = output_df.loc[output_df['new_model'] >= value.percent].sort_values('new_model', ascending=False).head(value.limit)
    if output.empty:
        detail = "no data found for your request"
        error = ErrorRequest(404, detail, '127.0.0.1', os.getcwd() + '\\' + os.path.basename(__file__))
        await error.write_log_errors()    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    return {
        'most_similar': output.to_dict()['new_model']
        }