import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv


from router.admin import router as admin_router

from database.database import session_local, engine
from database import crud, model, schemas


model.base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()


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


@app.get("/user", response_model=schemas.UserTest)
def get_user(user: schemas.UserTest, db: Session = Depends(get_db)):
    return crud.get_user(db, user=user)


@app.post("/user", response_model=schemas.UserTest)
def create_user(user: schemas.UserTest, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)
