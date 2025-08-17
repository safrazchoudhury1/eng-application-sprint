# Project Overview

This mini-project simulates an unstable-internet uploader. The script `retry_logger.py` attempts to upload a job with exponential backoff and logs each attempt to `upload_log.txt`.

## Running the script

From the root of this repository, run:

```
python project/retry_logger.py
```

This will perform a demo upload with simulated failures and generate `upload_log.txt` inside the `project/` directory. Open the log file to see each attempt timestamp and final status.

## Future Improvements

- Add command-line arguments to specify job parameters.
- Visualize the retry timeline from the log.
- Build a simple user interface to monitor jobs.
