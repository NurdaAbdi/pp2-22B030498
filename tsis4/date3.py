from datetime import datetime
def drop_micro(dt):
    return dt.replace(microsecond=0)
today = datetime.now()
print(drop_micro(today))
