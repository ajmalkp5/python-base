# linear searching

lst=[10,20,3,5,4,7,23]
# element=int(input("enter element"))

# is_present=False

# for i in range (0,len(lst)):
#     cur_element=lst[i]
#     if cur_element==element:
#         is_present=True
#         break

# print(is_present)

# linear searching easy way

lst=[10,20,3,5,4,7,23]

lst.sort()

element=int(input("enter element"))
is_present=False
low=0
upp=len(lst)-1

while(low<=upp):

    mid=(low+upp)//2

    if element==lst[mid]:

        is_present=True
        break
    elif element < lst[mid]:
        upp=mid-1

    elif element > lst[mid]:
        low=mid+1
print(is_present)    