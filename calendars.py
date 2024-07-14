# Anoushka Saha
# Calendars
# Python for Data Analysis
# July 13th, 2024

# Importing necessary modules
import calendar

# Create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2025, 1, 0, 0)
print(str)

# Create a HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# hstr = hc.formatmonth(2025, 1)
# print(hstr)

# Loop over days of the month
for i in c.itermonthdays(2024, 7):
    print(i)

# Calendar module utilities for locale
for month in calendar.month_name:
    print(month)

for day in calendar.day_name:
    print(day)

# Monthly team meetings on first Friday schedule
print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2024, m)
    week1 = cal[0]
    week2 = cal[1]

    if week1[calendar.FRIDAY] != 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]

    print(calendar.month_name[m], meetday)