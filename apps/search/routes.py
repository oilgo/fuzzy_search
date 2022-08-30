from fastapi import APIRouter, status
from .services import _get_values
from .schemas import SearchRequest


router = APIRouter(
    prefix = "/search", 
    tags = ["Fuzzy search"])


@router.post(
    path = "/extract", 
    status_code = status.HTTP_200_OK)
async def get_values(
    request: SearchRequest
):
    """ Endpoint to return similar values
    """

    response = await _get_values(
        value = request)

    return response