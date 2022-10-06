from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session


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


app = FastAPI(
    # 잠시 주석 처리
    # root_path="/admin" if os.getenv("DEV_SERV") else None,
    # docs_url="/docs" if os.getenv("ENV") == "dev" else None,
    # redoc_url="/redoc" if os.getenv("ENV") == "dev" else None,
    # openapi_url="/openapi.json" if os.getenv("ENV") == "dev" else None,
)
# CORS 미들웨어
origins = [
    "http://localhost:8000",
    # 나중 frontend url 추가
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# router
app.include_router(admin_router)


# 나중에 삭제해야함.
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user", response_model=schemas.UserTest)
def get_user(user: schemas.UserTest, db: Session = Depends(get_db)):
    return crud.get_user(db, user=user)


@app.post("/user", response_model=schemas.UserTest)
def create_user(user: schemas.UserTest, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)
