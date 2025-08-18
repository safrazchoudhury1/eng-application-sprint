import threading
from project import retry_logger_concurrent as rc


def test_thread_safe_logging(tmp_path):
    rc.LOG_FILE = tmp_path / "log.txt"
    rc.LOG_FILE.write_text("")

    def worker():
        rc.write_log("hello")

    threads = [threading.Thread(target=worker) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    lines = rc.LOG_FILE.read_text().strip().splitlines()
    assert len(lines) == 5
