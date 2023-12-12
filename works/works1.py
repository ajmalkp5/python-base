# write a program to display "hello" if a number enterd by user is a multipple of five,otherwise print bye
# using if else

# num=int(input("write a number"))

# if num %5==0:
#     print("hello")
# else:
#     print("bye")



# write a program to check whether a person is eligible for voting or not
# using if else

# age=int(input("enter your age"))

# if age>=18:
#     print("you are eligible for voting")
# else:
#     print("you are not eligible for voting")


# Write a program to accept percentage from the user and display the grade according to the following criteria:
# Mark > 90 =A Grade
# >80 and <= 90 = B Grade
# >=60 and <= 80 =C Grade
# Below 60 = D grade

# using if elif

# mark=int(input("enter your mark"))

# if mark>90:
#     print("A grade")
# elif mark>80: #and mark<=90:
#     print("B grade")
# elif mark>=60 and mark<=80:
#     print("C grade")
# else:
#     print("D grade")


# write a program to find the largest number out of three numbers excepted from user

num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))

if num1>num2 and num1>num3:
    print(f"{num1} number is largest")
elif num2>num1 and num2>num3:
    print(f"{num2} number is largest")
elif num3>num1 and num3>num2:
    print(f"{num3} number is largest")
elif num1==num2 and num1==num3:
    print("all are equal")




     