# total number of words

f=open("C:\\Users\\ASUS\Desktop\\my python\\fileio\\file2.txt","r")
wc={}

for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
print(wc)
            