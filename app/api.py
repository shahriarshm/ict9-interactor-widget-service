import jinja2
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import HTMLResponse
from uuid import UUID

from app.models import Widget, WidgetInteraction
from app.schemas import WidgetCreate, WidgetUpdate, WidgetInteractionCreate, WidgetInteractionStats
from typing import List, Dict
from app.deps import verify_api_key
from app.services import auth_service
from datetime import datetime, timedelta

protected_router = APIRouter(dependencies=[Depends(verify_api_key)])
public_router = APIRouter()

# Protected routes
@protected_router.post("/widgets", response_model=Widget)
async def create_widget(widget: WidgetCreate):
    new_widget = Widget(**widget.dict())
    await new_widget.insert()
    return new_widget

@protected_router.put("/widgets/{widget_id}", response_model=Widget)
async def update_widget(widget_id: UUID, widget_update: WidgetUpdate):
    widget = await Widget.find_one(Widget.widget_id == widget_id)
    if not widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    
    update_data = widget_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(widget, field, value)
    
    await widget.save()
    return widget

@protected_router.delete("/widgets/{widget_id}")
async def delete_widget(widget_id: UUID):
    widget = await Widget.find_one(Widget.widget_id == widget_id)
    if not widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    await widget.delete()
    return {"message": "Widget deleted successfully"}

# Public routes
@public_router.post("/widgets/{widget_id}/interactions", response_model=WidgetInteraction)
async def create_widget_interaction(interaction: WidgetInteractionCreate):
    new_interaction = WidgetInteraction(**interaction.dict())
    await new_interaction.insert()
    return new_interaction

@public_router.get("/widgets/{widget_id}/interactions", response_model=List[WidgetInteraction])
async def get_widget_interactions(widget_id: UUID, client_reference_id: str = None, current_user: dict = Depends(auth_service.get_current_user)):
    widget = await Widget.find_one(Widget.widget_id == widget_id)
    if not widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    
    query = {"widget_id": widget_id}
    if client_reference_id:
        query["client_reference_id"] = client_reference_id
    
    return await WidgetInteraction.find(query).to_list()

@public_router.get("/widgets/{widget_id}/stats", response_model=WidgetInteractionStats)
async def get_widget_interaction_stats(widget_id: UUID, days: int = 30, current_user: dict = Depends(auth_service.get_current_user)):
    widget = await Widget.find_one(Widget.widget_id == widget_id)
    if not widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    interactions = await WidgetInteraction.find({
        "widget_id": widget_id,
        "timestamp": {"$gte": start_date, "$lte": end_date}
    }).to_list()
    
    total_interactions = len(interactions)
    unique_clients = len(set(interaction.client_reference_id for interaction in interactions))
    
    return WidgetInteractionStats(
        widget_id=widget_id,
        total_interactions=total_interactions,
        unique_clients=unique_clients,
        time_period_days=days
    )


@public_router.get("/widgets/{widget_id}/unique-interactors", response_model=Dict[str, List[WidgetInteraction]])
async def get_unique_widget_interactors(widget_id: UUID, current_user: dict = Depends(auth_service.get_current_user)):
    widget = await Widget.find_one(Widget.widget_id == widget_id)
    if not widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    
    interactions = await WidgetInteraction.find(
        WidgetInteraction.widget_id == widget_id
    ).to_list()
    
    grouped_interactions = {}
    for interaction in interactions:
        client_id = interaction.client_reference_id
        if client_id:
            if client_id not in grouped_interactions:
                grouped_interactions[client_id] = []
            grouped_interactions[client_id].append(interaction)
    
    return grouped_interactions

@public_router.get("/widgets/{widget_id}/html", response_class=HTMLResponse)
async def get_widget_html(widget_id: UUID):
    widget = await Widget.find_one(Widget.widget_id == widget_id)
    if not widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    
    template = jinja2.Template(widget.body)
    rendered_html = template.render(**widget.config)
    
    return HTMLResponse(content=rendered_html, status_code=200)

# Combine routers
router = APIRouter()
router.include_router(protected_router)
router.include_router(public_router)
