from urllib import response
from fastapi import APIRouter, status
from .services import get_similar_values
from .validations import SearchRequest

router = APIRouter(prefix='/search', tags=['fuzzy search'])

@router.post(path='/extract', status_code=status.HTTP_200_OK)
async def get_values(request: SearchRequest):
    """cool"""
    response = await get_similar_values(value=request)
    return response