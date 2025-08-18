import time
from project import retry_logger_gui as gui


def test_gui_upload_with_retries(monkeypatch):
    calls = []

    def fake_attempt(path):
        calls.append(path)
        return True

    monkeypatch.setattr(gui, "attempt_upload", fake_attempt)
    monkeypatch.setattr(gui, "log", lambda msg: None)
    monkeypatch.setattr(time, "sleep", lambda s: None)
    assert gui.upload_with_retries("job", max_retries=3, base_delay=0) is True
    assert calls == ["job"]
