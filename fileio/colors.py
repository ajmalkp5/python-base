path="C:\\Users\\ASUS\\Desktop\\my python\\fileio\\colors.txt"

f=open(path,"w")

colors=["red","blue","green"]

for c in colors:
    f.write(c+"\n")