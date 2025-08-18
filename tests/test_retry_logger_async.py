import pytest
from project import retry_logger_async


@pytest.mark.asyncio
async def test_async_upload_with_retries(monkeypatch):
    calls = 0

    async def fake_attempt(job_id):
        nonlocal calls
        calls += 1
        return calls >= 2

    monkeypatch.setattr(retry_logger_async, "attempt_upload", fake_attempt)
    monkeypatch.setattr(retry_logger_async, "write_log", lambda msg: None)
    result = await retry_logger_async.upload_with_retries(
        1, max_retries=3, base_delay=0
    )
    assert result is True
    assert calls == 2
