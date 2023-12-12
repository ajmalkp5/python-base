# 1.Write a program to accept two numbers and mathematical operators and perform operation accordingly
# Output:
# Enter 1st number :10
# Enter 2nd number:5
# Enter operator: -
# The answer:5

# if elif statements


# num1=int(input("enter a num"))
# num2=int(input("enter a num"))
# operators=(input("enter operators"))

# if operators=='+':
#     add=num1+num2
#     print(add)
# elif operators=='-':
#     sub=num1-num2
#     print(sub)
# elif operators=='*':
#     mult=num1*num2
#     print(mult)
# elif operators=='/':
#     div=num1/num2
#     print(div)

# 2. Take input of age of 3 people by user and determine oldest and youngest among them.
#difficult way

# if elif

# age1=int(input("enter age:"))
# age2=int(input("enter age:"))
# age3=int(input("enter age:"))

# if age1>age2 and age1>age3:
#     if age3>age1:
#         print(f"{age3} oldest {age1} youngest")
#     else:
#         print(f"{age1} oldest {age2} youngest")
# elif age2>age1 and age2>age3:
#     if age1>age2:
#         print(f"{age1} oldest {age2} youngest")
#     else:
#         print(f"{age2} oldest {age3} youngest")
# elif age3>age1 and age3>age2:
#     if age2>age3:
#          print(f"{age2} oldest {age3} youngest")
#     else:
#         print(f"{age3} oldest {age1} youngest")

# simple way
# age1=int(input("enter age:"))
# age2=int(input("enter age:"))
# age3=int(input("enter age:"))

# if age1>age2 and age1>age3:
#     print(f"{age1} oldest")
# elif age2>age1 and age2>age3:
#     print(f"{age2} oldest")
# elif age3>age1 and age3>age2:
#     print(f"{age3} oldest")

# if age1<age2 and age1<age3:
#     print(f"{age1} youngest")
# elif age2<age1 and age2<age3:
#     print(f"{age2} youngest")
# elif age3<age1 and age3<age2:
#     print(f"{age3} youngest")

# easy method

# max min method

age1=int(input("enter age:"))
age2=int(input("enter age:"))
age3=int(input("enter age:"))

oldest=max(age1,age2,age3)
youngest=min(age1,age2,age3)

print("oldes person is",oldest,"years old")
print("youngest person",youngest,"years old")


# 3. Take values of length and breadth of a rectangle from user and check if it is square or not.

# if else

# len=int(input("enter a length:"))
# brdth=int(input("enter a breadth:"))

# if len==brdth:
#     print("it is a square")
# else:
#     print("it is not a square")


