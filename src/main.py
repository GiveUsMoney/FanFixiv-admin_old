import os

from fastapi import FastAPI

from dotenv import load_dotenv

load_dotenv() 

app = FastAPI(
    docs_url='/docs' if os.getenv("ENV") == 'dev' else None
)


@app.get("/")
async def root():
    return {"message": "Hello World"}