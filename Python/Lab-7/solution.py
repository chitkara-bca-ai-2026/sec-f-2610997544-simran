print("=== CALENDAR VERIFICATION SYSTEM ===")

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Enter a positive year.")
else:
    if year % 400 == 0:
        is_leap_year = True
        reason = "Divisible by 400"
    elif year % 100 == 0:
        is_leap_year = False
        reason = "A century year not divisible by 400"
    elif year % 4 == 0:
        is_leap_year = True
        reason = "Divisible by 4 and not a century year"
    else:
        is_leap_year = False
        reason = "Not divisible by 4"

    if is_leap_year:
        print("Year:", year)
        print("Status: LEAP YEAR")
        print("Days in year: 366")
        print("Days in February: 29")
    else:
        print("Year:", year)
        print("Status: COMMON YEAR")
        print("Days in year: 365")
        print("Days in February: 28")

    print("Reason:", reason) 