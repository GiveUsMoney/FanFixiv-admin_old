import os

from fastapi import FastAPI

from dotenv import load_dotenv

load_dotenv() 

app = FastAPI(
    root_path="/admin" if os.getenv("DEV_SERV") else None,
    docs_url='/docs' if os.getenv("ENV") == 'dev' else None,
    redoc_url="/redoc" if os.getenv("ENV") == 'dev' else None,
    openapi_url="/openapi.json" if os.getenv("ENV") == 'dev' else None,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}