import httpx
import pytest

BASE_URL = "http://localhost:8000"


@pytest.mark.asyncio
async def get_auth_token():
    login_data = {"username": "admin", "password": "."}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/api/token/", data=login_data)
        return response.json().get("access")
