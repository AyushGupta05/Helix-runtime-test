import json
from pathlib import Path

from app.models.settings import WebhookSettings


SETTINGS_PATH = Path(__file__).resolve().parents[3] / "data" / "settings.json"


def load_settings() -> dict:
    with SETTINGS_PATH.open("r", encoding="utf-8") as file:
        raw_settings = json.load(file)

    return {
        "webhook_url": raw_settings["webhook_url"],
        "retry_enabled": raw_settings.get("retry_enabled", True),
        "retry_delay_seconds": raw_settings.get("retry_delay_seconds", 30),
        "max_retries": raw_settings.get("max_retries", 3),
    }


def save_settings(payload: WebhookSettings) -> dict:
    stored = {
        "webhook_url": str(payload.webhook_url),
        "retry_enabled": payload.retry_enabled,
        "retry_delay_seconds": payload.retry_delay_seconds,
        "max_retries": payload.max_retries,
    }

    with SETTINGS_PATH.open("w", encoding="utf-8") as file:
        json.dump(stored, file, indent=2)

    return payload.model_dump()


def compute_retry_schedule(retry_delay_seconds: int, max_retries: int) -> list[int]:
    return [retry_delay_seconds for _ in range(max_retries)]

