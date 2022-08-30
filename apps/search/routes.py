from fastapi import APIRouter, status
from .services import decider
from .schemas import SearchRequest


router = APIRouter(
    prefix = "/search", 
    tags = ["fuzzy search"])


@router.post(
    path = "/extract", 
    status_code = status.HTTP_200_OK)
async def get_values(
    request: SearchRequest
):
    """ Endpoint to return similar values
    """

    response = await decider(
        value = request)

    return response


