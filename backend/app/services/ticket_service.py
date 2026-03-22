import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "tickets.json"


def list_tickets() -> list[dict]:
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def update_ticket(ticket_id: str, changes: dict) -> dict | None:
    tickets = list_tickets()

    for index, ticket in enumerate(tickets):
        if ticket["id"] == ticket_id:
            tickets[index] = {**ticket, **changes}
            with DATA_PATH.open("w", encoding="utf-8") as file:
                json.dump(tickets, file, indent=2)
            return tickets[index]

    return None
