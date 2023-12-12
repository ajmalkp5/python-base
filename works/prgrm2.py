# print all non century years from starting year to current year

start_year=int(input("enter starting year"))

current_year=2023

i=start_year

while(i<=current_year):
    year=i
    if year%100!=0:
        print(year)
    i+=1    
