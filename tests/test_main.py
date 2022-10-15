from utils import imp

imp()

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World"}

#  유저의 jwt 검증 확인.
def test_admin_verity():
    response = client.get("/admin")
    assert response.status_code == 200
    assert response.json() == {"Cookle의 값": None}
