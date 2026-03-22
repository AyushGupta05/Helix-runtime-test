def test_summary_honors_resolved_filter(client):
    response = client.get("/tickets/summary", params={"status": "resolved"})

    assert response.status_code == 200
    assert response.json()["open_tickets"] == 0
    assert response.json()["overdue"] == 0
    assert response.json()["at_risk"] == 0


def test_summary_honors_status_and_priority_filters(client):
    response = client.get("/tickets/summary", params={"status": "open", "priority": "medium"})

    assert response.status_code == 200
    assert response.json() == {
        "open_tickets": 2,
        "overdue": 1,
        "at_risk": 1,
    }
