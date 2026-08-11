from datetime import datetime, timedelta

def next_due_at(rating, now):
    days = rating ** 2
    due = now + timedelta(days=days)
    return due.isoformat()