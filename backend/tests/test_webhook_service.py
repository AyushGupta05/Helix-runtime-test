import json
import tempfile
from pathlib import Path
from unittest.mock import patch
from app.models.settings import WebhookSettings
from app.services.webhook_service import load_settings, save_settings


def test_webhook_settings_persistence():
    """Test that webhook settings are saved and loaded with consistent keys."""
    with tempfile.TemporaryDirectory() as tmpdir:
        settings_path = Path(tmpdir) / "settings.json"

        # Create initial settings file
        initial_data = {
            "webhook_url": "https://example.com/webhook",
            "retry_enabled": True,
            "retry_delay_seconds": 30,
            "max_retries": 3,
        }
        with settings_path.open("w") as f:
            json.dump(initial_data, f)

        # Mock the SETTINGS_PATH
        with patch("app.services.webhook_service.SETTINGS_PATH", settings_path):
            # Load settings
            loaded = load_settings()
            assert loaded["webhook_url"] == "https://example.com/webhook"
            assert loaded["retry_enabled"] is True
            assert loaded["retry_delay_seconds"] == 30
            assert loaded["max_retries"] == 3

            # Save modified settings
            modified = WebhookSettings(
                webhook_url="https://example.com/webhook",
                retry_enabled=False,
                retry_delay_seconds=60,
                max_retries=5,
            )
            saved = save_settings(modified)
            assert saved["retry_enabled"] is False
            assert saved["retry_delay_seconds"] == 60
            assert saved["max_retries"] == 5

            # Load again to verify persistence
            reloaded = load_settings()
            assert reloaded["retry_enabled"] is False
            assert reloaded["retry_delay_seconds"] == 60
            assert reloaded["max_retries"] == 5
