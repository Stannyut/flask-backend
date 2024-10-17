# utils/helpers.py

from datetime import datetime

def format_datetime(dt):
    if dt:
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    return None