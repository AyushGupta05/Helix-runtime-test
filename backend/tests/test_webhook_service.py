import json
from pathlib import Path

from app.services.webhook_service import compute_retry_schedule


def test_retry_schedule_uses_fixed_delay_today():
    assert compute_retry_schedule(30, 3) == [30, 30, 30]


def test_load_settings_supports_legacy_retry_keys():
    settings_path = Path(__file__).resolve().parents[2] / "data" / "settings.json"
    settings_path.write_text(
        json.dumps(
            {
                "webhook_url": "https://hooks.example.internal/support-events",
                "retry_enabled": False,
                "retryDelay": 90,
                "maxRetries": 6,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    from app.services.webhook_service import load_settings

    assert load_settings() == {
        "webhook_url": "https://hooks.example.internal/support-events",
        "retry_enabled": False,
        "retry_delay_seconds": 90,
        "max_retries": 6,
    }
