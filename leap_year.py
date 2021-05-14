year = int(input("Enter a year, I'll tell u is a leap year or not :"))
if not year % 4 and year % 100 != 0 or not year % 400 :
    print("This year is leap year! ")
else: print("This year is not leap year!")
