from pydantic import BaseModel, HttpUrl


class WebhookSettings(BaseModel):
    webhook_url: HttpUrl
    retry_enabled: bool
    retry_delay_seconds: int
    max_retries: int

