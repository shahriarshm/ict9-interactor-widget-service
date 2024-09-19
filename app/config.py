from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mongodb://mongodb:27017/widgetdb"
    API_V1_STR: str = "/api/v1"
    API_TOKEN: str = "widget-service-token"
    AUTH_SERVICE_URL: str = "http://192.168.1.15:8000/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()