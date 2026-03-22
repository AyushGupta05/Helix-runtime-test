from pydantic import BaseModel


class Ticket(BaseModel):
    id: str
    customer: str
    status: str
    priority: str
    created_at: str
    first_response_due_at: str
    assigned_to: str


class TicketUpdate(BaseModel):
    status: str
    assigned_to: str | None = None
