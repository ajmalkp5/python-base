# 1.Write a program to print 10,8,6,4,2,0,-2,-4,-6,-8,-10

# using for loop

# for num in range(10,-11,-2):
#     print(num,end=",")


# 2. Write a program to print sum of even number in a range

# for loop

# num1=int(input("enter 1st number:"))
# num2=int(input("enter 2nd number:"))

# sum=0

# for i in range(num1,num2+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)



# 3. Write a program to calculate BMI and give message ‘’over weight,underweight,healthy

# decision making

weight_inkg=int(input("enter wight in kg"))

heightin_cm=int(input("enter height in cm"))

heightin_meter=heightin_cm/100

bmi=weight_inkg/heightin_meter**2
print(f"bmi={bmi}")


# bmi<19=underweight
# 19-25=healthy
# 25-30=overweight



if bmi>=25 and bmi<30:
    print("over weight")
elif  bmi<19:
    print("under weight")
elif bmi>=18.5 and bmi<25:
    print("healthy")
