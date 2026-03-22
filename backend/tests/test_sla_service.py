import pytest
from datetime import UTC, datetime
from app.services.sla_service import summarize_tickets


def test_summarize_tickets_respects_status_filter():
    """Test that status filter is applied correctly."""
    tickets = [
        {
            "id": "1",
            "status": "open",
            "priority": "high",
            "first_response_due_at": "2026-03-20T19:00:00Z",
        },
        {
            "id": "2",
            "status": "pending",
            "priority": "high",
            "first_response_due_at": "2026-03-20T19:00:00Z",
        },
        {
            "id": "3",
            "status": "resolved",
            "priority": "high",
            "first_response_due_at": "2026-03-20T19:00:00Z",
        },
    ]

    # Filter by status="open" should only include ticket 1
    result = summarize_tickets(tickets, status="open")
    assert result["open_tickets"] == 1
    assert result["overdue"] == 0
    assert result["at_risk"] == 1

    # Filter by status="pending" should only include ticket 2
    result = summarize_tickets(tickets, status="pending")
    assert result["open_tickets"] == 1

    # No status filter should include tickets 1 and 2 (resolved excluded)
    result = summarize_tickets(tickets)
    assert result["open_tickets"] == 2


def test_summarize_tickets_respects_priority_filter():
    """Test that priority filter is applied correctly."""
    tickets = [
        {
            "id": "1",
            "status": "open",
            "priority": "high",
            "first_response_due_at": "2026-03-20T19:00:00Z",
        },
        {
            "id": "2",
            "status": "open",
            "priority": "low",
            "first_response_due_at": "2026-03-20T19:00:00Z",
        },
    ]

    result = summarize_tickets(tickets, priority="high")
    assert result["open_tickets"] == 1

    result = summarize_tickets(tickets, priority="low")
    assert result["open_tickets"] == 1


def test_summarize_tickets_combined_filters():
    """Test that status and priority filters work together."""
    tickets = [
        {
            "id": "1",
            "status": "open",
            "priority": "high",
            "first_response_due_at": "2026-03-20T19:00:00Z",
        },
        {
            "id": "2",
            "status": "open",
            "priority": "low",
            "first_response_due_at": "2026-03-20T19:00:00Z",
        },
        {
            "id": "3",
            "status": "pending",
            "priority": "high",
            "first_response_due_at": "2026-03-20T19:00:00Z",
        },
    ]

    result = summarize_tickets(tickets, status="open", priority="high")
    assert result["open_tickets"] == 1

    result = summarize_tickets(tickets, status="pending", priority="high")
    assert result["open_tickets"] == 1
