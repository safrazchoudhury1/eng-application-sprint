#!/usr/bin/env python3
"""
retry_logger_concurrent.py
Simulates concurrent uploads with retries and exponential backoff, writing logs to upload_log_concurrent.txt.

Usage:
    python retry_logger_concurrent.py --jobs 3 --max-retries 5
"""

import time
import random
import datetime
import pathlib
import threading
import argparse

LOG_FILE = pathlib.Path(__file__).parent / "upload_log_concurrent.txt"
log_lock = threading.Lock()

def attempt_upload(job_id: int) -> bool:
    """Simulate upload success with 70% success rate."""
    return random.random() < 0.7

def write_log(message: str) -> None:
    """Thread-safe append to log file with timestamp."""
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    with log_lock:
        LOG_FILE.write_text((LOG_FILE.read_text() if LOG_FILE.exists() else "") + f"[{timestamp}] {message}\n", encoding="utf-8")

def upload_with_retries(job_id: int, max_retries: int = 5, base_delay: float = 0.5):
    delay = base_delay
    for attempt in range(1, max_retries + 1):
        success = attempt_upload(job_id)
        write_log(f"job {job_id}: attempt {attempt} -> {'OK' if success else 'FAIL'}")
        if success:
            write_log(f"job {job_id}: COMPLETED")
            return True
        time.sleep(delay)
        delay *= 2
    write_log(f"job {job_id}: GAVE UP")
    return False

def worker(job_id: int, max_retries: int):
    upload_with_retries(job_id, max_retries)

def run_concurrent_jobs(num_jobs: int, max_retries: int):
    threads = []
    for job_id in range(1, num_jobs + 1):
        t = threading.Thread(target=worker, args=(job_id, max_retries), daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def parse_args():
    parser = argparse.ArgumentParser(description="Simulate concurrent unreliable uploads with retries.")
    parser.add_argument("--jobs", type=int, default=3, help="Number of concurrent upload jobs.")
    parser.add_argument("--max-retries", type=int, default=5, help="Maximum retries per job.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.seed is not None:
        random.seed(args.seed)
    write_log("===== New run started =====")
    run_concurrent_jobs(args.jobs, args.max_retries)
    write_log("===== All jobs finished =====")
    print(f"Completed {args.jobs} jobs. See {LOG_FILE} for details.")
