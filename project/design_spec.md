# Unstable Internet Uploader: Design Specification

## Problem statement
The unstable‑internet uploader is designed to ensure files and data are reliably uploaded even when the network connection is intermittent. In environments with frequent power or connectivity outages, uploads may fail mid‑transfer. This tool manages these failures transparently.

## Objectives
- **Robustness**: Ensure every queued upload is eventually delivered.
- **Efficiency**: Avoid unnecessary network traffic and retries.
- **Transparency**: Log each attempt for auditing and debugging.

## Architecture
- **Job Queue**: A persistent queue (file‑based) stores the upload jobs. Each job records the file path, destination URL and state. Using a file‑backed queue ensures tasks survive process restarts.
- **Worker**: A worker function reads jobs from the queue and attempts to upload them. If an upload fails, the job remains in the queue for a retry.
- **Retry Strategy**: Use exponential backoff (e.g., initial delay 0.5 s multiplied by 2 each retry) with a maximum number of retries. Exponential backoff reduces load during outages compared to fixed intervals.
- **Concurrency**: To handle multiple uploads concurrently, a thread pool or an asyncio event loop can process multiple jobs at once. Concurrency improves throughput when the network is stable.
- **Logging**: All attempts, successes and failures are written to a log file with timestamps. This log can be analysed to compute success rates and diagnose failures.

## Trade‑offs
- **Queue Storage**: In‑memory queues are fast but lose data on restart. A file‑based queue is slower but survives crashes. We choose a simple file‑backed JSON or CSV queue for reliability.
- **Threaded vs. Async**: Threads are simple but each blocked I/O call occupies a thread. Async I/O scales better but is more complex. We provide both a threaded and an async implementation to illustrate the trade‑offs.
- **Backoff Policy**: Exponential backoff reduces network congestion but increases delay to completion. A fixed delay is simpler but can overload the network during outages.

## Future enhancements
- **GUI**: Provide a simple Tkinter GUI to select files, view queue status and monitor progress.
- **Web API**: Expose a Flask/FastAPI endpoint so uploads can be requested over HTTP.
- **Unit Tests & CI**: Write tests for the queue, retry logic and concurrency handling, and add a GitHub Actions workflow to run them on each commit.
- **Real‑Time Feedback**: Integrate progress bars or notifications to inform users of the upload status.
