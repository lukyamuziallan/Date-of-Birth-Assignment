"""
    Program that outputs date of birth,
    including the exact day of the week,
    given the user's age and birthday
"""

import calendar

age = int(input("Age: "))
month = int(input("Month of birth (1 - 12): "))
date = int(input("Date of birth (1 - 31): "))
current_year = int(input("Current Year: "))

year = current_year - age
day = calendar.weekday(year, month, date)
day_string = calendar.day_name[day]

print("You were born on a " + day_string + " in the year " + str(year))
