from pydantic import BaseModel
from typing import Optional
from uuid import UUID

from app.models import WidgetInteractionType

class WidgetCreate(BaseModel):
    widget_id: UUID
    host_id: UUID
    campaign_id: UUID
    body: str
    config: dict

class WidgetUpdate(BaseModel):
    body: Optional[str] = None
    config: Optional[dict] = None

class WidgetInteractionCreate(BaseModel):
    widget_id: UUID
    client_refrence_id: str
    ref_url: str
    interaction_type: WidgetInteractionType
    interaction_data: dict

class WidgetInteractionStats(BaseModel):
    widget_id: UUID
    total_interactions: int
    unique_clients: int
    time_period_days: int