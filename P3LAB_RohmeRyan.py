# Ryan Rohme
# March 12, 2024
# P3LAB
# how to write code that displays information to users

is_leap_year = False
   
input_year = int(input())

if input_year % 4 == 0:
    # Check if the year is a century year and not divisible by 400
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True

if is_leap_year:
    print(input_year, "- leap year")
else:
    print(input_year, "- not a leap year")
