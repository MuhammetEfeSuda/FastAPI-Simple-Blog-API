import pytest
from fastapi.testclient import TestClient
from index import app
from bson import ObjectId


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    # Add test data
    post_data = {
        "title": "Test Post",
        "short_description": "Short desc",
        "description": "Detailed description",
        "tags": ["test"]
    }
    response = client.post("/", json=post_data)
    post_id = response.json()["id"]
    yield client, post_id
    # Clear test data
    client.delete(f"/{post_id}")


def test_get_all_posts(test_app):
    client, _ = test_app
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_post_by_id(test_app):
    client, post_id = test_app
    response = client.get(f"/{post_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert response_data["id"] == post_id


def test_create_post(test_app):
    client, _ = test_app
    new_post = {
        "title": "Another Post",
        "short_description": "Another short desc",
        "description": "Another detailed description",
        "tags": ["another"]
    }
    response = client.post("/", json=new_post)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == new_post["title"]
    assert response_data["short_description"] == new_post["short_description"]
    assert response_data["description"] == new_post["description"]
    assert response_data["tags"] == new_post["tags"]


def test_update_post(test_app):
    client, post_id = test_app
    updated_post = {
        "title": "Updated Title",
        "short_description": "Updated short description.",
        "description": "Updated description.",
        "tags": ["updated", "post"]
    }
    response = client.put(f"/{post_id}", json=updated_post)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == updated_post["title"]
    assert response_data["short_description"] == updated_post["short_description"]
    assert response_data["description"] == updated_post["description"]
    assert response_data["tags"] == updated_post["tags"]


def test_delete_post(test_app):
    client, post_id = test_app
    response = client.delete(f"/{post_id}")
    assert response.status_code == 200
    assert "id" in response.json()
