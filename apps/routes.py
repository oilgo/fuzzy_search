from fastapi import APIRouter
from .search.routes import router as search_router

router = APIRouter(prefix='/API')

router.include_router(search_router)