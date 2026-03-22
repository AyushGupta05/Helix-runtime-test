# support-ops-dashboard

A small internal support dashboard for a SaaS team. It combines a React frontend with a FastAPI backend to help agents review support tickets, understand SLA risk, and manage webhook settings for downstream tooling.

## Product summary

- Ticket dashboard with filtering by status and priority
- SLA summary cards for at-risk and overdue work
- Settings page for webhook integration behavior
- Backend endpoints for ticket listing, ticket summary, and settings updates

## Run locally

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API starts on `http://127.0.0.1:8000`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The Vite app starts on `http://127.0.0.1:5173`.

## Tests

### Backend tests

```bash
cd backend
pytest
```

### Frontend tests

```bash
cd frontend
npm test
```

## Known workflow

1. Start the backend.
2. Start the frontend.
3. Open the dashboard.
4. Filter tickets by status and priority.
5. Visit Settings to configure webhook delivery behavior.

Webhook retries should use exponential backoff so downstream providers are not overwhelmed during incidents.

## Demo prompt

Use this prompt in the demo:

> Can you investigate and fix the reliability issues in this support dashboard? The SLA summary looks inconsistent when filtering tickets, and webhook retry settings don’t seem to persist correctly. Please trace the problems end to end, make the code changes directly, validate everything with tests, use Civic guardrails for the important decisions and tool use, and leave the result ready for human review.

