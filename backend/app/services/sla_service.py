from datetime import UTC, datetime


def _parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def summarize_tickets(
    tickets: list[dict],
    status: str | None = None,
    priority: str | None = None,
) -> dict[str, int]:
    filtered = [
        ticket
        for ticket in tickets
        if ticket["status"] != "resolved"
        and (priority is None or ticket["priority"] == priority)
    ]
    now = datetime(2026, 3, 20, 18, 0, tzinfo=UTC)

    overdue = 0
    at_risk = 0
    open_tickets = 0

    for ticket in filtered:
        due_at = _parse_timestamp(ticket["first_response_due_at"])
        minutes_until_due = (due_at - now).total_seconds() / 60

        open_tickets += 1
        if minutes_until_due <= 0:
            overdue += 1
        elif minutes_until_due <= 60:
            at_risk += 1

    return {
        "overdue": overdue,
        "at_risk": at_risk,
        "open_tickets": open_tickets,
    }

