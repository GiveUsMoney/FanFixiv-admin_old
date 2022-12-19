import tests.db

import pytest

from fastapi.testclient import TestClient

from src.main import app
from src.database import SessionLocal

from src.entity.tag import Tag
from src.enum.tag_type import TagType

client = TestClient(app)

session = SessionLocal()

tag1 = {
    "type": TagType.CHARACTOR,
    "name": "테스트 태그 1",
    "description": "테스트 태그에 대한 설명",
    "status": False,
    "is_adult": False,
}
tag2 = {
    "type": TagType.CHARACTOR,
    "name": "테스트 태그 2",
    "description": "테스트 태그에 대한 설명",
    "status": True,
    "is_adult": False,
}
tag3 = {
    "type": TagType.CHARACTOR,
    "name": "테스트 태그 3",
    "description": "테스트 태그에 대한 설명",
    "status": True,
    "is_adult": False,
}

tags = [tag1, tag2, tag3]

headers = {"Authorization": "Bearer test"}


@pytest.mark.order(1)
def test_tag_post_200():
    for tag in tags:
        req = client.post("/tag", json=tag, headers=headers)
        assert req.status_code == 200


@pytest.mark.order(1)
def test_tag_post_400():
    tag = tag1.copy()
    del tag["status"]
    req = client.post("/tag", json=tag, headers=headers)
    assert req.status_code == 400


#


@pytest.mark.order(2)
def test_tag_list_200():
    req = client.get("/tag/list", headers=headers)
    assert req.status_code == 200

@pytest.mark.order(2)
def test_tag_list_400():
    req = client.get("/tag/list", params={"limit": "test"}, headers=headers)
    assert req.status_code == 400


#


@pytest.mark.order(3)
def test_update_status_200():
    content = client.get("/tag/list", headers=headers).json()
    seq = content[0]['Tag']['seq']

    req = client.put(f"/tag/status/{seq}?status=true", headers=headers)
    assert req.status_code == 200


@pytest.mark.order(3)
def test_update_status_400():
    req = client.put(f"/tag/status/test", headers=headers)
    assert req.status_code == 400


#


@pytest.mark.order(4)
def test_tag_update_200():
    content = client.get("/tag/list", headers=headers).json()
    seq = content[0]['Tag']['seq']

    tag = tag1.copy()
    tag["name"] = "변경된 테스트 태그 1"

    req = client.put(f"/tag/{seq}", json=tag, headers=headers)
    assert req.status_code == 200


@pytest.mark.order(4)
def test_tag_update_400():
    req = client.put(f"/tag/test", headers=headers)
    assert req.status_code == 400

    content = client.get("/tag/list", headers=headers).json()
    seq = content[0]['Tag']['seq']

    tag = {
        "status" : "test"
    }

    req = client.put(f"/tag/{seq}", json=tag, headers=headers)
    assert req.status_code == 400


#


@pytest.mark.order(5)
def test_tag_delete_200():
    content = client.get("/tag/list", headers=headers).json()
    seq = content[0]['Tag']['seq']

    req = client.delete(f"/tag/{seq}", headers=headers)
    assert req.status_code == 200


@pytest.mark.order(5)
def test_tag_delete_400():
    req = client.delete(f"/tag/test", headers=headers)
    assert req.status_code == 400


#


@pytest.mark.order(10)
def test_remove_all_tags():
    result = session.query(Tag).delete()
    session.commit()
    assert True
