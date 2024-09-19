from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

from app.config import settings


api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != settings.API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key