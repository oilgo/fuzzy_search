import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from .validations import SearchRequest

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

async def get_similar_values(value: SearchRequest):
    '''returns similar values from the database'''
    df = pd.read_csv(f'./apps/database/{value.file_name}')
    models = list(df.ModelName)
    length = len(models)
    similarity_list = [0] * length
    for i in range(length):
        similarity_list[i] = round(similar(value.new_model, models[i]) * 100, value.round)
    output = pd.DataFrame(np.asarray(similarity_list), index=models, columns=['new_model']).sort_values('new_model', ascending=False).head(value.limit)
    return {
        'most_similar': output.to_dict()['new_model']
        }