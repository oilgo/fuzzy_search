from fastapi import FastAPI
from starlette.responses import RedirectResponse
from apps.routes import router as API

app = FastAPI()

app.include_router(API)

@app.get("/")
def read_root():
    return RedirectResponse(url='/docs/')
