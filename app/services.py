from fastapi.security import OAuth2PasswordBearer
import httpx
from typing import Dict, Any
from fastapi import Depends, HTTPException
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthService:
    def __init__(self):
        self.base_url = settings.AUTH_SERVICE_URL

    async def get_current_user(self, token: str = Depends(oauth2_scheme)) -> Dict[str, Any]:
        url = f"{self.base_url}/users/me"

        headers = {"Authorization": f"Bearer {token}"}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
        return self._handle_response(response)

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="Widget not found")
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Widget service error: {response.text}",
            )


auth_service = AuthService()
