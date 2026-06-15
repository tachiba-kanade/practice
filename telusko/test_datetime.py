from datetime import *

def leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if leap(year) else 28

    if month in [4, 6, 9, 11]:
        return 30
    return 31
    
def cal_dob():
    dob = input( "Enter the DOB in format dd/mm/yyyy: ").split('/')
    dob_day = int(dob[0])
    dob_month = int(dob[1])
    dob_year = int(dob[2])

    now = datetime.now()
    current_day = now.day
    current_month = now.month
    current_year = now.year

    if current_day < dob_day:
        current_month -= 1

        if current_month == 0:
            current_month = 12
            current_year -= 1

        current_day += days_in_month(current_month, current_year)

    diff_day = current_day - dob_day

    # Borrow months if needed
    if current_month < dob_month:
        current_month += 12
        current_year -= 1

    diff_month = current_month - dob_month

    diff_year = current_year - dob_year 


    print(f"YOU ARE  {diff_year} YEARS {diff_month} MONTHS  {diff_day} DAYS OLD  ")

    user_input = input("NOW do you want in details like down to hours, seconds and mili seconds (yes or no):" ).lower()

    if user_input == "yes":
        print("Continuing the program...")
    elif user_input == "no":
        print("Exiting the program.")
    else:
        print("Invalid response. Please enter yes or no.")
    
    details = input( "Enter the details of birth in hours(0-23), mins(0-59), second(0-59) and milliseconds(0-999) in in format hh/mm/ss/mmmm: ").split('/')
    dob_hour = int(details[0])
    dob_min = int(details[1])
    dob_second = int(details[2])
    dob_milli = int(details[3])

    hours = now.hour
    minutes = now.minute
    seconds = now.second
    # Python tracks microseconds (1/1,000,000), so divide by 1000 for milliseconds for datetime
    milliseconds = now.microsecond // 1000
    
    # Milliseconds
    diff_milli = milliseconds - dob_milli
    if diff_milli < 0:
        diff_milli += 1000
        milliseconds -= 1

    # Seconds
    diff_sec = seconds - dob_second
    if diff_sec < 0:
        diff_sec += 60
        minutes -= 1

    # Minutes
    diff_min = minutes - dob_min
    if diff_min < 0:
        diff_min += 60
        hours -= 1

    # Hours
    diff_hour = hours - dob_hour
    if diff_hour < 0:
        diff_hour += 24
        current_day -= 1
    print(f"YOU ARE {diff_year} YEARS {diff_month} MONTHS {diff_day} DAYS {diff_hour} HOURS {diff_min} MINUTES {diff_sec} SECONDS {diff_milli} MILLISECONDS OLD")



cal_dob()
