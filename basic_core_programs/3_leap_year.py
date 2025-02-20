# Program to check if year is leap year or not

# Function that cheaks for leap year
def leap_year(year:int):
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False

# Taking input from the user
year=int(input("Enter the year: "))

if len(str(year))!=4:
    print('Invalid year')
else:
    result=leap_year(year)
    if result == True:
        print(f'{year} is a Leap year')
    else:
        print(f'{year} is not a Leap year')