# 2 number give largest compare

#input two numbers
num1 =int(input("enter the first number: "))
num2 = int(input("enter the second number:"))

# compare the numbers
if num1>num2:
    print(f"{num1} is the largest number")
elif num2>num1:
    print(f"{num2} is the largest number")
else:
    print("both numbers are eqaul:")    
