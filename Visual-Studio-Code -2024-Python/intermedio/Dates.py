#Dates

from datetime import datetime

fecha = datetime(2024, 3, 16, 4, 3, 34)

print(fecha.second)

now = datetime.now()

print(now.minute)

from datetime import time

my_time = time(3, 45)

print(my_time.minute)

from datetime import date

my_date = date.today

print(my_date.day)


new_year = datetime(2024, 4, 5)

print(new_year - now)