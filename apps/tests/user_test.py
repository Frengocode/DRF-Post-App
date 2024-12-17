from apps.tests.confest import get_auth_token, BASE_URL
import pytest
import httpx



@pytest.mark.asyncio
async def test_create_user():
    data = {
        "username": "jackson",
        "password1": "admin123321",
        "password2": "admin123321"
    }

    async with httpx.AsyncClient() as cl:
        response = await cl.post(f"{BASE_URL}/user/api/v1/create-user/", json=data)
        assert response.status_code == 201



