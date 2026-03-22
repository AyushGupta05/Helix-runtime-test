import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_data_files():
    settings_path = Path(__file__).resolve().parents[2] / "data" / "settings.json"
    tickets_path = Path(__file__).resolve().parents[2] / "data" / "tickets.json"
    original = {
        "webhook_url": "https://hooks.example.internal/support-events",
        "retry_enabled": True,
        "retry_delay_seconds": 30,
        "max_retries": 3,
    }
    original_tickets = tickets_path.read_text(encoding="utf-8")
    settings_path.write_text(json.dumps(original, indent=2), encoding="utf-8")
    yield
    settings_path.write_text(json.dumps(original, indent=2), encoding="utf-8")
    tickets_path.write_text(original_tickets, encoding="utf-8")
