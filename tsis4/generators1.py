from datetime import datetime
d1 = datetime(2023, 12, 4)
d2 = datetime(2022, 5, 26)
def diff(d1, d2):
    dif = d1 - d2
    return dif.total_seconds()
print(f'The difference in seconds is: {diff(d1, d2)} seconds')
