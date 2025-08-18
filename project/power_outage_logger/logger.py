"""
Power Outage Logger

This script reads a CSV file with start and end timestamps for power outages and calculates the duration of each outage and the total downtime.

Usage:
    python power_outage_logger/logger.py power_outage_logger/outages.csv

The CSV file should have headers `start` and `end` with timestamps in the format YYYY-MM-DD HH:MM.
"""

import csv
from datetime import datetime, timedelta
from typing import Iterable, List, Tuple


def parse_time(ts: str) -> datetime:
    """Parse a timestamp string into a datetime object."""
    return datetime.strptime(ts.strip(), "%Y-%m-%d %H:%M")


def read_outages(filepath: str) -> list[tuple[datetime, datetime]]:
    """Read outage intervals from a CSV file.

    Each row must have two columns: 'start' and 'end'.
    Returns a list of (start, end) tuples.
    """
    outages: list[tuple[datetime, datetime]] = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            start = parse_time(row["start"])
            end = parse_time(row["end"])
            if end < start:
                raise ValueError(f"End time {end} is before start time {start}.")
            outages.append((start, end))
    return outages


def merge_outages(
    outages: Iterable[tuple[datetime, datetime]],
) -> list[tuple[datetime, datetime]]:
    """Merge overlapping or adjacent outage intervals."""
    sorted_outages = sorted(outages, key=lambda x: x[0])
    merged: List[Tuple[datetime, datetime]] = []
    for start, end in sorted_outages:
        if not merged or start > merged[-1][1]:
            merged.append((start, end))
        else:
            last_start, last_end = merged[-1]
            merged[-1] = (last_start, max(last_end, end))
    return merged


def summarize(outages: Iterable[tuple[datetime, datetime]]) -> None:
    """Print a summary of merged outages and total downtime."""
    merged = merge_outages(outages)
    total_downtime = timedelta()
    print("Outage summary:")
    for i, (start, end) in enumerate(merged, 1):
        duration = end - start
        total_downtime += duration
        print(f"{i}. Start: {start}, End: {end}, Duration: {duration}")
    print(f"Total downtime: {total_downtime}")


def main():  # pragma: no cover
    import argparse

    parser = argparse.ArgumentParser(description="Summarize power outage durations.")
    parser.add_argument("csvfile", help="Path to CSV file with outage start/end times")
    args = parser.parse_args()
    outages = read_outages(args.csvfile)
    summarize(outages)


if __name__ == "__main__":  # pragma: no cover
    main()
