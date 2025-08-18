from datetime import datetime
import pytest
from project.power_outage_logger import logger


def test_merge_overlapping_outages():
    a = (datetime(2025, 1, 1, 0, 0), datetime(2025, 1, 1, 1, 0))
    b = (datetime(2025, 1, 1, 0, 30), datetime(2025, 1, 1, 2, 0))
    merged = logger.merge_outages([a, b])
    assert merged == [(a[0], b[1])]


def test_merge_empty_list():
    assert logger.merge_outages([]) == []


def test_merge_unordered_input():
    a = (datetime(2025, 1, 1, 0, 30), datetime(2025, 1, 1, 1, 0))
    b = (datetime(2025, 1, 1, 0, 0), datetime(2025, 1, 1, 0, 45))
    merged = logger.merge_outages([a, b])
    assert merged == [(datetime(2025, 1, 1, 0, 0), datetime(2025, 1, 1, 1, 0))]


def test_merge_adjacent_one_minute_windows():
    a = (datetime(2025, 1, 1, 0, 0), datetime(2025, 1, 1, 0, 1))
    b = (datetime(2025, 1, 1, 0, 1), datetime(2025, 1, 1, 0, 2))
    merged = logger.merge_outages([a, b])
    assert merged == [(a[0], b[1])]


def test_read_outages_and_summarize(tmp_path, capfd):
    csv_file = tmp_path / "outages.csv"
    csv_file.write_text(
        "start,end\n2025-01-01 00:00,2025-01-01 00:01\n2025-01-01 02:00,2025-01-01 03:00\n"
    )
    outages = logger.read_outages(str(csv_file))
    logger.summarize(outages)
    out = capfd.readouterr().out
    assert "Total downtime" in out
    assert "0:01:00" in out


def test_read_outages_invalid_order(tmp_path):
    csv_file = tmp_path / "bad.csv"
    csv_file.write_text("start,end\n2025-01-01 01:00,2025-01-01 00:00\n")
    with pytest.raises(ValueError):
        logger.read_outages(str(csv_file))
