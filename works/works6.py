# 1. Write a Python program that accepts a string and calculates the number of digits and letters.

text=input("enter the string")
dig_cnt=0
alpha_cnt=0
for w in text:
    if w.isdigit()==True:
        dig_cnt+=1
    elif w.isalpha()==True:
        alpha_cnt+=1
print(f"number of digits={dig_cnt}")
print(f"number of letters={alpha_cnt}")



# 2.Write a python program to display multiplication table of a number (user input)

# num=int(input("enter number"))
# for i in range(1,11):
#     print(f"{i}*{num}={i*num}")


# 3.Pattern print
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# for row in range(1,6):
#     for col in range(1,row+1):
#         print(row,end="\t")
#     print()