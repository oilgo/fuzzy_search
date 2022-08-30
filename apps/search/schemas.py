from pydantic import BaseModel
from typing import Optional


class SearchRequest(BaseModel):
    """
    """

    name: str
    new_model: str
    limit: Optional[int] = 10
    round: Optional[int] = 2
    percent: Optional[float] = 50
    type: str

    class Config:
        schema_extra = {
            "example": {
                "name": 'EquipmentModel',
                "new_model": 'СКАТ-2400',
                "limit": 10,
                "round": 2,
                "percent": 50,
                "type": 'database'
            }
        }