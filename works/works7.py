# 1. Write a Python program that separate positive and negative numbers from a list


# fst=[6,3,-4,9,-2,5,-1,2]
# pve_num=[]
# nve_num=[]

# for i in range(0,len(fst)):
#     if fst[i]>0:
#         pve_num.append(fst[i])
#     elif fst[i]<0:
#         nve_num.append(fst[i])
# print(f"positive number={pve_num}")
# print(f"negative number={nve_num}")



# 2.Write a python program to reverse the tuple

tpl=(50,70,30,14,67,85,32,54)
tp_rvrse=[]
for i in range(len(tpl)-1,-1,-1):
    tp_rvrse.append(tpl[i])
tp_rvrse=tuple(tp_rvrse)
print(tp_rvrse)




# 3.Pattern print
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4  
# 5


# for row in range(1,6):
#     for col in range(row,6):
#         print(row,end=" ")
#     print() 
