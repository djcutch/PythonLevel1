import datetime
from datetime import date
# date(year, month, day)
currentdate = datetime.date(2019, 11, 12)
birthday = datetime.date(1983, 4, 8)
ageindays = (currentdate-birthday)
print("age", ageindays)
print ()
