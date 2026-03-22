from fastapi import APIRouter, HTTPException, Query

from app.models.ticket import TicketUpdate
from app.services.sla_service import summarize_tickets
from app.services.ticket_service import list_tickets, update_ticket

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("")
def get_tickets():
    return list_tickets()


@router.get("/summary")
def get_ticket_summary(
    status: str | None = Query(default=None),
    priority: str | None = Query(default=None),
):
    tickets = list_tickets()
    return summarize_tickets(tickets, status=status, priority=priority)


@router.patch("/{ticket_id}")
def patch_ticket(ticket_id: str, payload: TicketUpdate):
    updated = update_ticket(ticket_id, payload.model_dump(exclude_none=True))
    if updated is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return updated
