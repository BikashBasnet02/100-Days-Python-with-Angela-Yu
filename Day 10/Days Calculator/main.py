def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))

    if month > 12 or month < 1:
        print("Invalid month")
        return
    
    if month == 2 and is_leap(year):
        print("29 days")
    else:
        print(month_days[month - 1])

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Test the function
days_in_month()
