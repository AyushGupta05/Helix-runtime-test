def test_ticket_list_returns_seed_data(client):
    response = client.get("/tickets")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 24
    assert payload[0]["id"] == "TCK-1001"

