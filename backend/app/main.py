from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.settings import router as settings_router
from app.routes.tickets import router as tickets_router

app = FastAPI(title="Support Ops Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets_router)
app.include_router(settings_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

