# Power Outage Logger

This mini-project analyzes power outage events. It reads a CSV file (`outages.csv`) containing the start and end timestamps of outages and computes the duration of each outage and the total downtime.

## Files

- `outages.csv` — sample dataset recording outage start and end times.
- `logger.py` — Python script that reads the CSV, calculates durations, and prints a summary.

## Usage

Run the script from the repository root (or with the correct relative paths) using Python 3:

```
python project/power_outage_logger/logger.py project/power_outage_logger/outages.csv
```

The script outputs each outage’s start and end times, the duration of each outage, and the total downtime across all outages.

## What I learned

- Reading structured CSV data using Python’s `csv.DictReader`.
- Parsing timestamps with the `datetime` module.
- Calculating time differences with `timedelta` and summarizing them.
- Building simple command-line utilities with argument parsing.
