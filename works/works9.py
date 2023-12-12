# 1. Write a Python program to find leap year (user input)

# year=int(input("enter year"))

# if year %100==0 and year %4==0 or year %100!=0 and year %4==0:
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not a leap year")



# 2.Write a python program to sum all the items in the dictionary 

# items={"apple":30,"pineaple":21,"orange":15,"grape":17}
# total_sum=sum(items.values())

# print(total_sum)


# 3.Pattern print 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *

for row in range(1,6):
    for col in range(1,4):
        print("*",end="\t")
    print()