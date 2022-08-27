from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from apps.routes import router as api
from core.database import database, metadata, engine


app = FastAPI()

metadata.create_all(
    bind = engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

app.include_router(
    router = api)


@app.get("/")
async def main():
    return RedirectResponse(
        url = "/docs/")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()