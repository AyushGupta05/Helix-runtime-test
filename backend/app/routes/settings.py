from fastapi import APIRouter

from app.models.settings import WebhookSettings
from app.services.webhook_service import load_settings, save_settings

router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("")
def get_settings():
    settings = load_settings()
    return {
        "webhook_url": settings["webhook_url"],
        "retry_enabled": settings["retry_enabled"],
        "retry_delay_seconds": settings["retry_delay_seconds"],
        "max_retries": settings["max_retries"],
    }


@router.put("")
def update_settings(payload: WebhookSettings):
    result = save_settings(payload)
    return {
        "webhook_url": result["webhook_url"],
        "retry_enabled": result["retry_enabled"],
        "retry_delay_seconds": result["retry_delay_seconds"],
        "max_retries": result["max_retries"],
    }

