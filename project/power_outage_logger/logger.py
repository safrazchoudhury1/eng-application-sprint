"""
Power Outage Logger

This script reads a CSV file with start and end timestamps for power outages and calculates the duration of each outage and the total downtime.

Usage:
    python power_outage_logger/logger.py power_outage_logger/outages.csv

The CSV file should have headers `start` and `end` with timestamps in the format YYYY-MM-DD HH:MM.
"""
import csv
from datetime import datetime, timedelta

def parse_time(ts: str) -> datetime:
    """Parse a timestamp string into a datetime object."""
    return datetime.strptime(ts.strip(), "%Y-%m-%d %H:%M")

def read_outages(filepath: str):
    """Read outage intervals from a CSV file.

    Each row must have two columns: 'start' and 'end'.
    Returns a list of (start, end) tuples.
    """
    outages = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            start = parse_time(row['start'])
            end = parse_time(row['end'])
            if end < start:
                raise ValueError(f"End time {end} is before start time {start}.")
            outages.append((start, end))
    return outages

def summarize(outages):
    """Print a summary of outages and total downtime."""
    total_downtime = timedelta()
    print("Outage summary:")
    for i, (start, end) in enumerate(outages, 1):
        duration = end - start
        total_downtime += duration
        print(f"{i}. Start: {start}, End: {end}, Duration: {duration}")
    print(f"Total downtime: {total_downtime}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Summarize power outage durations.")
    parser.add_argument("csvfile", help="Path to CSV file with outage start/end times")
    args = parser.parse_args()
    outages = read_outages(args.csvfile)
    summarize(outages)

if __name__ == "__main__":
    main()
