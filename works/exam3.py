str1=input("enter a string1")
str2=input("enter a string2")

smallest_lngth=min(len(str1),len(str2))

result=""
for i in range(0,smallest_lngth):
    out=str1[i]+str2[i]
    result+=out

# slicing
    
if len(str1)>len(str2):
    rem=str1[smallest_lngth:]

else:
    rem=str2[smallest_lngth:]

result+=rem
print(result)

