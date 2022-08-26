import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from .validations import SearchRequest
from fastapi import HTTPException, status

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

async def get_similar_values(value: SearchRequest):
    '''returns similar values from the database'''
    try:
        df = pd.read_csv(f'./apps/database/{value.file_name}')
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"file {value.file_name} not found")
    models = list(df.ModelName)
    length = len(models)
    similarity_list = [0] * length
    for i in range(length):
        similarity_list[i] = round(similar(value.new_model, models[i]) * 100, value.round)
    output_df = pd.DataFrame(np.asarray(similarity_list), index=models, columns=['new_model'])
    output = output_df.loc[output_df['new_model'] >= value.percent].sort_values('new_model', ascending=False).head(value.limit)
    return {
        'most_similar': output.to_dict()['new_model']
        }