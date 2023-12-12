age=25 # int
# type
print(type(age))

name="ajmal" # string
print(type(name))

is_vaccinated=True # boolean= True or False
print(type(is_vaccinated))

total=123.507 # float
print(type(total))


fh=int(input("enter the value"))
deg=(fh-32)*(5/9)
print(f"{fh} fh is equal to {deg} degree")

#
selling_prize=int(input("enter the selling price"))
cost_prize=int(input("enter the value of cost prize"))
profit=selling_prize-cost_prize
print(f"the profit is {profit}")
profit_in_percentage=(profit/cost_prize)*100
print(f"the profit percentage is {profit_in_percentage}")

# calculate bmi
height_in_cm=int(input("enter the value in cm"))
weight_in_kg=(input("enter weight in kg"))
height_in_meter=(height_in_cm/100)
bmi=(weight_in_kg/height_in_meter**2)
print(f"your bmi is {bmi}")

