# write all year 1800 - 22024

path="C:\\Users\\ASUS\\Desktop\\my python\\fileio\\years.txt"

f=open(path,"w")

for i in range(1800,2025):
    f.write(str(i)+"\n")

# read years from year.txt and write all leap years

path="C:\\Users\\ASUS\\Desktop\\my python\\fileio\\years.txt"

f=open(path,"r")
for line in f:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year % 100!=0 and year%4==0:
        print(year)



# write all leap years to leap year.text

read_path="C:\\Users\\ASUS\\Desktop\\my python\\fileio\\years.txt"
write_path="C:\\Users\\ASUS\\Desktop\\my python\\fileio\\leap_year.txt"

fr=open(read_path,"r")
fw=open(write_path,"w")

for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year % 100!=0 and year%4==0:
        fw.write(str(year)+"\n")

