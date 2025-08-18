from project import retry_logger_concurrent_v2 as rc


def test_run_jobs_writes_completion(tmp_path, monkeypatch):
    rc.LOG_FILE = tmp_path / "log.txt"

    def always_success(job_id):
        return True

    monkeypatch.setattr(rc, "attempt_upload", always_success)
    rc.run_jobs(num_jobs=2, max_retries=2, base_delay=0)
    content = rc.LOG_FILE.read_text()
    assert "COMPLETED" in content
