# 1.Write a python program to convert the temperature in degree centigrade to fahrenheit


# degree_c=int(input("enter the temperature "))

# fahrenheit=(degree_c*9/5)+32

# print(f"fahrenheit is {fahrenheit}")


# 2. Write a python program to find compound interest

# A=amount
# p=principle
# r=rate
# y=year
# n=no.of times intrest applied

# A=P(1+r/n)^nt

P=int(input("enter the principle balance "))
r=float(input("enter the rate "))
n=int(input("enter the no .of times interst applied "))
y=int(input("enter the year "))
A=P*(1+r/n)**(n*y)
compound_intrest=A-P

print(compound_intrest)


# 3. Write a python program to find area of a circle.

pi=3.14

r=int(input("enter the radius "))

area_of_circle=pi*(r*r)

print(area_of_circle)