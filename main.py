from fastapi import FastAPI
from starlette.responses import RedirectResponse
from apps.routes import router as API
from core.database import database

app = FastAPI()

app.include_router(API)


@app.get("/")
async def read_root():
    return RedirectResponse(url='/docs/')


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

