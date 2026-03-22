from fastapi import APIRouter

from app.models.settings import WebhookSettings
from app.services.webhook_service import load_settings, save_settings

router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("")
def get_settings():
    return load_settings()


@router.put("")
def update_settings(payload: WebhookSettings):
    return save_settings(payload)

