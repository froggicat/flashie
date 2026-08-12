from datetime import datetime
from scheduler import next_due_at


def test_rating_3_is_nine_days_later():
    # Fixed "now" so the test doesn't depend on the real clock
    now = datetime(2026, 8, 8, 12, 0, 0)
    result = next_due_at(3, now)
    assert result == datetime(2026, 8, 17, 12, 0, 0).isoformat()


def test_rating_1_is_one_day_later():
    now = datetime(2026, 8, 8, 12, 0, 0)
    result = next_due_at(1, now)
    assert result == datetime(2026, 8, 9, 12, 0, 0).isoformat()


def test_rating_5_is_twenty_five_days_later():
    now = datetime(2026, 8, 8, 12, 0, 0)
    result = next_due_at(5, now)
    # 2nd of september
    assert result == datetime(2026, 9, 2, 12, 0, 0).isoformat()
