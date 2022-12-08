from dotenv import load_dotenv

load_dotenv()

import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import config

from src.rabbit.rabbit import consume

from src.tag import tag_router
from src.admin.router import router as admin_router

app = FastAPI(
    root_path="/admin" if config.DEV_SERV == "true" else None,
    docs_url="/docs" if config.ENV == "dev" else None,
    redoc_url="/redoc" if config.ENV == "dev" else None,
    openapi_url="/openapi.json" if config.ENV == "dev" else None,
)
# CORS 미들웨어
origins = [
    "*",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    loop = asyncio.get_event_loop()
    # use the same loop to consume
    asyncio.ensure_future(consume(loop))


# router
app.include_router(tag_router)
app.include_router(admin_router)
