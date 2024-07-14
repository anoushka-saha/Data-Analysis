# Anoushka Saha
# Dates & Times
# Python for Data Analysis
# July 13th, 2024

# Importing necessary modules
from datetime import date, time, datetime, timedelta

# Getting today's date
today = date.today()
print("Today's date: ", today)

# Printing date components
print("Date components: ", today.day, today.month, today.year)

# Today's weekday number
print("Today's weekday number is: ", today.weekday())
days = ["monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
print("Which is a", days[today.weekday()])

# Getting today's date using datetime
today_dt = datetime.now()
print("The current date and time is", today_dt)

# Getting current time
time = datetime.time(datetime.now())
print("The current time is:", time)

# Takes string argument with formatting codes
print(today_dt.strftime("The current year is: %Y"))
print(today_dt.strftime("The current weekday is: %A"))
print(today_dt.strftime("The current month is: %B"))
print(today_dt.strftime("The current day of the month is: %d"))

# Locale's date and time
print(today_dt.strftime("Locale date and time: %c"))
print(today_dt.strftime("Locale date: %x"))
print(today_dt.strftime("Locale time: %X"))

# Time formatting
print(today_dt.strftime("Current time: %I:%M:%S %p"))
print(today_dt.strftime("24-hour time: %H:%M"))

# Constructing a basic timedelta
print(timedelta(days = 365, hours = 5, minutes = 1))

# Print today's date one year from now
print("One year from now it will be", str(today_dt + timedelta(days = 365)))

# Timedelta with multiple arguments
print("In two weeks and 3 days it will be: ", str(today_dt + timedelta(weeks = 2, days = 3)))

# Calculate the date 1 week ago
print("One week ago it was: ", str(today_dt - timedelta(weeks = 1)))

# How many days until April Fools?
td = date.today()
afd = date(td.year, 4, 1)

if afd < td:
    print("April Fool's Day already went by: ", ((td - afd).days))
    afd = afd.replace(year = td.year + 1)

time_to_afd = afd - td
print("It is", time_to_afd.days," days until the next April Fool's Day!")