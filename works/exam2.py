str1="ABC"
str2="POI"

result=""

for i in range(0,len(str1)):
    out=str1[i] + str2[i]
    result+=out

print(result)