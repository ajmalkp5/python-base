#leapyear
starting_year=1000
current_year=2024
for year in range(starting_year,current_year):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)