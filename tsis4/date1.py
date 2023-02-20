from datetime import datetime, timedelta
today = datetime.now()
def subt(date, days):
    return date - timedelta(days=days)
print(f'The date is: {subt(today, 5)}')
