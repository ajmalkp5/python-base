# 1. Write a python program to create a list of tuples having first element as the number and second element as the cube of the number

# fst=[]
# for num in range(1,5):
#     number=int(input("enter the number :"))
#     fst.append((num,num**3))
# print(fst)

# 2. find the length of the string using for loop

# name="ajmal"

# string_count=0
# for i in name:
#     string_count+=1

# print(f"length of the string is {string_count}")



# 3. Write a program to handling missing keys


data={'a':1, 'b':2, 'c':3}
key=input("enter the key")
if key in data:
    print(data[key])
else:
    print("key not found")

# 4.Pattern print 
#         A 
#        B C 
#       D E F 
#      G H I J 
#     K L M N O

# i=65
# for row in range(1,6):
#     for col1 in range(1,6-row):
#         print(end=" ")
#     for col2 in range(1,row+1):
#         print(chr(i),end=" ")
#         i+=1
#     print(" ")
