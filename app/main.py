from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import Widget, WidgetInteraction
from app.config import settings
from app.api import router as api_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(database=client.db_name, document_models=[Widget, WidgetInteraction])

@app.get("/")
async def root():
    return {"message": "Welcome to the Widget Service API"}

app.include_router(api_router, prefix=settings.API_V1_STR)


