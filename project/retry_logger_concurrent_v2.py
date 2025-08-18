import argparse
import random
import datetime
import pathlib
import concurrent.futures
import time
from typing import Optional

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
    write_log(f"job {job_id}: exhausted retries")
    return False

def run_jobs(num_jobs: int, max_retries: int, base_delay: float) -> None:
    """Run multiple jobs concurrently."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(upload_with_retries, job_id, max_retries, base_delay): job_id
            for job_id in range(1, num_jobs + 1)
        }
        for future in concurrent.futures.as_completed(futures):
            job_id = futures[future]
            success = future.result()
            write_log(f"job {job_id}: {'COMPLETED' if success else 'GAVE UP'}")

def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simulate uploads with retries and backoff.")
    parser.add_argument("--jobs", type=int, default=1, help="Number of jobs to run concurrently")
    parser.add_argument("--max-retries", type=int, default=5, help="Maximum retries per job")
    parser.add_argument("--base-delay", type=float, default=0.5, help="Initial delay in seconds before retrying")
    return parser.parse_args(argv)

if __name__ == "__main__":
    args = parse_args()
    # Clear existing log so each run starts fresh
    LOG_FILE.write_text("", encoding="utf-8")
    run_jobs(args.jobs, args.max_retries, args.base_delay)
    print(f"Completed {args.jobs} job(s). See {LOG_FILE} for details.")
