import asyncio
import random
import datetime
import pathlib

# Async version of the unstable‑internet uploader
LOG_FILE = pathlib.Path(__file__).parent / "upload_log_async.txt"

def write_log(message: str) -> None:
    """Append a timestamped message to the async log file."""
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

async def attempt_upload(job_id: int) -> bool:
    """Simulate an upload attempt with a 50 % chance of success."""
    # In a real implementation, perform an async network call here.
    await asyncio.sleep(0)
    return random.random() > 0.5

async def upload_with_retries(job_id: int, max_retries: int = 5, base_delay: float = 0.5) -> bool:
    """Attempt to upload a job asynchronously with exponential backoff."""
    delay = base_delay
    for attempt in range(1, max_retries + 1):
        ok = await attempt_upload(job_id)
        write_log(f"job {job_id}: attempt {attempt} -> {'OK' if ok else 'FAIL'}")
        if ok:
            write_log(f"job {job_id}: COMPLETED")
            return True
        await asyncio.sleep(delay)
        delay *= 2
    write_log(f"job {job_id}: GAVE UP after {max_retries} retries")
    return False

async def run_jobs(num_jobs: int = 3) -> None:
    """Run multiple upload jobs concurrently using asyncio.gather."""
    tasks = [upload_with_retries(i + 1) for i in range(num_jobs)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    random.seed(42)  # Deterministic demo
    asyncio.run(run_jobs())
    print(f"Demo complete. See {LOG_FILE} for details.")
