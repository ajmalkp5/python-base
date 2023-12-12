# 1. Write a Python program to find the second largest number in a list.

# fst=[26,18,96,69,10]

# lrgst_num=0

# for num in fst:
#     if num>lrgst_num:
#         scnd_lrgst=lrgst_num
#         lrgst_num=num
#     elif num>scnd_lrgst and num!=lrgst_num:
#         scnd_lrgst=num
# if scnd_lrgst==num:
#     print("NO second largest")
# else:
#     print("second largest num is:", scnd_lrgst)




#     2. Write a program to filter the dictionary, from a dictionary of people’s heights and you wanted to filter out anyone below a certain height.

# Let’s filter out anyone less than 170cm.


heights={"aju":180,"usni":154,"dilu":160,"anu":176,"nabu":185}

for name, height in heights.items():
    if height>= 170:
        print(f"{name}:{height}")



# 3. Pattern print 
#                             4 4 4 4 4 4 4  
#                             4 3 3 3 3 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 2 1 2 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 3 3 3 3 4   
#                             4 4 4 4 4 4 4

# num=4
# for row in range(1,2*num):
#     for col in range(1,2*num):
#         print(max(row-3,col-3,2*num-row-3,2*num-col-3),end=" ")
#     print()