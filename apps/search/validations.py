from pydantic import BaseModel
from typing import Optional

class SearchRequest(BaseModel):
    file_name: str
    new_model: str
    limit: Optional[int] = 10
    round: Optional[int] = 2
    percent: Optional[float] = 50

    class Config:
        schema_extra = {
            'example': {
                'file_name': '_EquipmentModel__202208241757.csv',
                'new_model': 'СКАТ-2400',
                'limit': 10,
                'round': 2,
                'percent': 50
            }
        }
