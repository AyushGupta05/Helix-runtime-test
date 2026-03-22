def test_settings_round_trip_persists_retry_fields(client):
    payload = {
        "webhook_url": "https://hooks.example.internal/updated",
        "retry_enabled": True,
        "retry_delay_seconds": 45,
        "max_retries": 5,
    }

    save_response = client.put("/settings", json=payload)
    load_response = client.get("/settings")

    assert save_response.status_code == 200
    assert load_response.status_code == 200
    assert load_response.json()["retry_delay_seconds"] == 45
    assert load_response.json()["max_retries"] == 5

