from uuid import UUID
from beanie import Document, Indexed
from datetime import datetime
from pydantic import Field
from enum import Enum
from typing import Optional

class WidgetType(str, Enum):
    GAME = "game"
    SURVEY = "survey"
    QUIZ = "quiz"
    FORM = "form"
    CALCULATOR = "calculator"

class WidgetInteractionType(str, Enum):
    CLICK = "click"
    SUBMIT = "submit"
    CHANGE = "change"
    GAME_SCORE = "game_score"
    OTHER = "other"


class BaseModel(Document):
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())


class Widget(BaseModel):
    widget_id: UUID
    host_id: UUID
    campaign_id: UUID
    body: str
    config: dict

    class Settings:
        name = "widgets"


class WidgetInteraction(BaseModel):
    widget_id: UUID
    client_reference_id: Optional[str] = None
    ref_url: str
    interaction_type: WidgetInteractionType
    interaction_data: dict

    class Settings:
        name = "widget_interactions"
