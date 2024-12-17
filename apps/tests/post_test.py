import httpx
import pytest
from apps.tests.confest import get_auth_token, BASE_URL


@pytest.mark.asyncio
async def test_create_post():
    token = await get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    data = {"title": "Test Create Post"}

    async with httpx.AsyncClient() as cl:
        response = await cl.post(
            "http://localhost:8000/post/api/v1/create-post/", json=data, headers=headers
        )
        assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_posts():
    token = await get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as cl:
        response = await cl.get(f"{BASE_URL}/post/api/v1/get-posts/", headers=headers)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_post():
    token = await get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as cl:
        response = await cl.get(
            f"{BASE_URL}/post/api/v1/get-post/{5}/", headers=headers
        )
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_post():
    token = await get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as cl:
        response = await cl.patch(
            f"{BASE_URL}/post/api/v1/update-post/{5}/", headers=headers
        )
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_upost():
    token = await get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as cl:
        response = await cl.delete(
            f"{BASE_URL}/post/api/v1/delete-post/{4}/", headers=headers
        )
        assert response.status_code == 200
