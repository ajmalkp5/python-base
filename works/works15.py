# 1. Write a python program to find the sum of elements in a tuple

# tp=(12,10,5,5,7,3,3)

# sum=sum(list(tp))
# print(f"sum of the elements : {sum}")



# 2.Convert tuple to a list and find sum

# tp=(12,10,5,5,7,3,3)

# sum=0
# sum_list=[]

# tple=list(tp)
# print(tple)

# for i in tple:
#     sum=sum+i
# print(f"sum of the elements: {sum}")

# 3. Pattern print 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E


i=65
for row in range(1,6):
    for col in range(1,row+1):
        print(chr(i),end=" ")
    i+=1
    print("")