#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: "Nithurshan Raveendran"
The python code in this file (a1_nraveendran5.py) is original work written by
"Nithurshan Raveendran". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if month == 2: # February
        return 29 if leap_year(year) else 28  # February has 29 days in a leap year, 28 otherwise
    elif month in {4, 6, 9, 11}:
        return 30  # April, June, September, November have 30 days
    else:
        return 31  # All other months have 31 days

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''

    # Split the input date string into year, month, and day components.
    str_year, str_month, str_day = date.split('-')

    # Convert these string components to integers for calculations.
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    # Set the next day by incrementing the current day by 1
    tmp_day = day + 1  # next day

    # Check if the temporary day exceeds the maximum days in the month.
    if tmp_day > mon_max(month, year):
        # If it does, reset the day to 1 and move to the next month.
        to_day = 1
        tmp_month = month + 1
    else:
        # Otherwise, keep the incremented day and same month.
        to_day = tmp_day
        tmp_month = month

    # Check if the month exceeds 12, meaning we need to move to the next year.
    if tmp_month > 12:
        to_month = 1 # Reset the month to January
        year += 1 # Increment the year
    else:
        to_month = tmp_month

    # Format the result as YYYY-MM-DD with zero-padding for single-digit months/days.
    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date # Return the calculated next date


def usage():
    "Print a usage message to the user"
    print("Usage: python3 assignment1.py <start_date> <end_date>")
    print("Dates must be in YYYY-MM-DD format.")
    print("This program calculates the number of weekend days (Saturdays and Sundays) between two dates.")


def leap_year(year: int) -> bool:
    """Return True if the year is a leap year, False otherwise."""
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"

    # Initialize the weekend count
    weekend_count = 0
    current_date = start_date
    
    # Loop through each date from start_date to stop_date (inclusive)
    while current_date <= stop_date:
        # Get the day of the week for the current date
        year, month, day = map(int, current_date.split('-'))
        day_name = day_of_week(year, month, day)
        
        # Check if it's a weekend day (Saturday or Sunday)
        if day_name in ['sat', 'sun']:
            weekend_count += 1

        # Move to the next date
        current_date = after(current_date)

    return weekend_count

if __name__ == "__main__":
    ...