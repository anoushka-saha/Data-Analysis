# Anoushka Saha
# Dates & Times
# Python for Data Analysis
# July 13th, 2024

# Importing necessary modules
from datetime import date, time, datetime

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
