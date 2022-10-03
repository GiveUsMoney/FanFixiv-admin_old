import os
from fastapi import FastAPI
from dotenv import load_dotenv
from router.admin import router as admin_router


load_dotenv()

app = FastAPI(
    # 잠시 주석 처리
    # root_path="/admin" if os.getenv("DEV_SERV") else None,
    # docs_url="/docs" if os.getenv("ENV") == "dev" else None,
    # redoc_url="/redoc" if os.getenv("ENV") == "dev" else None,
    # openapi_url="/openapi.json" if os.getenv("ENV") == "dev" else None,
)
# admin_router 가져옴
app.include_router(admin_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
