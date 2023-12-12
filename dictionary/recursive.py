text="BCAGECABBAD"
# print first recursive character
wc={}

for ch in text:
    if ch in wc:
        print("first recursive of character",ch)
        break
    else:
        wc[ch]=1

# non repeating character

wc={}

for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

for k,v in wc.items():
    if (v==1):
        print(k)

# second recursive character

wc={}
dup_char=[]

for ch in text:
    if ch in wc:
        wc[ch]+=1
        dup_char.append(ch)
    else:
        wc[ch]=1
print(dup_char[1])

