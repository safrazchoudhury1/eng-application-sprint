import time
import random
import datetime
import pathlib

# Path to log file in the same directory as this script
LOG_FILE = pathlib.Path(__file__).parent / "upload_log.txt"


def attempt_upload(job_id: int) -> bool:
    """Simulate an upload; returns True if successful."""
    return random.random() > 0.5


def write_log(message: str) -> None:
    """Write a timestamped message to the log file."""
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def upload_with_retries(job_id: int, max_retries: int = 5, base_delay: float = 0.5) -> bool:
    """Attempt to upload with retries and exponential backoff."""
    delay = base_delay
    for attempt in range(1, max_retries + 1):
        success = attempt_upload(job_id)
        write_log(f"job {job_id}: attempt {attempt} -> {'OK' if success else 'FAIL'}")
        if success:
            return True
        time.sleep(delay)
        delay *= 2  # exponential backoff
    return False


if __name__ == "__main__":
    random.seed(42)  # deterministic for demo
    job_id = 1
    success = upload_with_retries(job_id)
    write_log(f"job {job_id}: {'COMPLETED' if success else 'GAVE UP'}")
    print(f"Finished with {'success' if success else 'failure'}. See upload_log.txt for details.")
