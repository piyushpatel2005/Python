# Working with Dates and Time

Use `datetime` module to work with dates and times. This is an object-oriented module.

**How to create date and time**

There are three constructors date(), time() and datetime().
You can also use today() and now() methods to create objects.

- `date.today()` : returns date object for current date.
- `datetime.now()` : returns datetime object for current date and time

**Constructors**

- `date(year, month, day)`
- `time([hour][,min][,sec][,microsec])` : All arguments are optional, if no argument given, they default to 0.
- `datetime(year, month, day[,hour][,min][,sec][,microsec])` : returns datetime object.

```python
from datetime import date, time, datetime
invoice_date = date.today()
invoice_date = datetime.now()
meeting_time = time(14, 20) # 2:30PM
halloween = date(1988, 10, 31)  # 10/31/1988
entry_time = datetime(2017, 10, 28, 14, 32, 48)
```

**Note:** Both datetime and time objects can be either aware or naive. Aware objects account for time zones and daylight savings time. Naive objects do not. By default, they are naive. You can make them aware by providing an optional `tzinfo` argument.

## Convert string to date time

You can use datetime.strptime() method to parse string to datetime.

- `datetime.strptime(datetime_str, format_str)` : uses specified format string to convert string to datetime object.

| Code | Description |
-------|:-----------:|
|%d | Day of the month as a number |
|%m | Month as a number  |
|%y | 2 digit year |
|%Y | 4 digit year |
|%H | Hour of day in 24 hour format |
|%M | Minutes |
|%S | Seconds |

```python
halloween = datetime.strptime("10/31/1988", "%m/%d/%Y")
date_str = input("Enter date of birth (MM/DD/YYYY): ")
birth_date = datetime.strptime(date_str, "%m/%d/%Y")
print("Date of birth: ", birth_date)  # It will display complete date with time 1985-07-28 00:00:00
```

# Formatting dates and times

- Use strftime() method of datetime to format date/time object.

- `strftime(format_str)` : uses specified format string to convert date/time object to formatted string.

| Code | Example |
|------|:--------:|
|%a | Sat |
|%A | Saturday |
|%b | Oct |
|%B | October |
|%d | 01 (zero padded day as number) |
|%m | 01 (zero padded month as number) |
|%Y | 2017 (4-digit year) |
|%y | 17 (2-digit year)|
|%H | 13 (24-hour format hour) |
|%I | 01 (Hour of day in 12-hour format) |
|%M | 59 (minutes) |
|%S | 59 (seconds) |
|%p | PM (AM/PM specifier) |
|%f | 01233 (microseconds) |
|%c | Mon Oct 31 01:15:15 2017 (Datetime formatted for locale) |
|%x | 31/10/2017 (date for locale) |
|%X | 01:15:15 (time for locale) |


```python
halloween.strftime("%B %d, %Y (%A)")  # October 31, 1988 (Monday)
halloween.strftime("%B %d, %I %M %p") # October 31, 10:48 PM
```

You can use timedelta object to work with a span of time.

**Constructor**

- `timedelta([days][, seconds][, microseconds][, milliseconds][, minutes][, hours][,weeks])`

```python
from datetime import timedelta
three_weeks = timedelta(weeks=3)
two_hours_thirty_minutes = timedelta(hours=2, minutes=30)
three_weeks_from_today = date.today() + timedelta(weeks=3)
three_hours_from_now = datetime.now() + timedelta(hours=3)
```

Timedelta object has following attributes and methods.

- `days` : number of days
- `seconds` : number of seconds in addition to days
- `microseconds` : number of microseconds in addition to days and seconds
- `total_seconds()` : total number of seconds and microseconds

```python
halloween = datetime(2017, 10, 31)
time_to_halloween = halloween - datetime.now()

days = time_to_halloween.days
```

[Invoice Due date example](../examples/invoice_duedate.py)

[Timer Program](../examples/timer.py)

Date/Time object has many attributes:

year, month, day, hour, minute, second, microsecond

```python
halloween = datetime(1988, 10, 31, 14, 32, 30)
year = halloween.year   # 1988
month = halloween.month   # 10
day = halloween.day # 31
hour = halloween.hour # 14
minute = halloween.minute   # 32
second = halloween.second # 30
microsecond = halloween.microsecond # 0
```

- You can compare two datetime objects using simple relational operators.

```python
today = date.today()
halloween = date(2017, 10, 31)
if today > halloween:
  print("Halloween 2017 has gone.")
elif today < halloween:
  print("Hwlloween 2017 is coming soon.")
elif today == halloween:
  print("Happy Halloween 2017")
```

```python
today = date.today()
halloween = date(today.year, 10, 31)
if today > halloween:
  next_year = today.year + 1
  halloween = date(next_year, 10, 31)
days_until = (halloween - today).days
print(days_until, "day(s) until Halloween.")
```

```python
meeting_start = datetime(2017, 12, 2, 9, 30)
meeting_end = meeting_start + timedelta(hours=1)
now = datetime.now()
if now > meeting_start and now < meeting_end:
  print("The meeting is happening now.")
elif now < meeting_start:
  print("This meeting is coming up.")
elif now > meeting_end:
  print("This meeting already took place.")
```

[Hotel Reservation Program](../examples/hotel_reservation.py)
