text="goodmorning"
charac_count={}

for ch in text:
    if ch in charac_count:
        charac_count[ch]+=1
    else:
        charac_count[ch]=1

print(charac_count)

