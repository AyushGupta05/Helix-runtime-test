from app.services.webhook_service import compute_retry_schedule


def test_retry_schedule_uses_fixed_delay_today():
    assert compute_retry_schedule(30, 3) == [30, 30, 30]
