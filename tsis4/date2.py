from datetime import datetime, timedelta
today = datetime.now()
def yesterday(date, days):
    return date - timedelta(days=days)
def tomorrow(date, days):
    return date + timedelta(days=days)
print(f'Yesterday was: {yesterday(today, 1)}')
print(f'Today is: {today}')
print(f'Tomorrow is: {tomorrow(today, 1)}')