from utils import imp

imp()

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# 이 커밋은 테스트용 커밋입니다.
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
