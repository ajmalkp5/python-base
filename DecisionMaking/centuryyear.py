# century year

# input year
year = int(input("enter a year: "))

# check if it is a century year
if year % 100 == 0:
    print(f"{year} is a centuary year")
else:
    print(f"{year} is a not century year")
