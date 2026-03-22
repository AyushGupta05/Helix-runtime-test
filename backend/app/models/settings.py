from pydantic import BaseModel, HttpUrl, Field


class WebhookSettings(BaseModel):
    webhook_url: HttpUrl
    retry_enabled: bool = Field(default=True)
    retry_delay_seconds: int = Field(default=30)
    max_retries: int = Field(default=3)

    class Config:
        populate_by_name = True

