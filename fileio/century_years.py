# write all century years to 1800 to 2024

path="C:\\Users\\ASUS\\Desktop\\my python\\fileio\\century_years.txt"

f=open(path,"w")

for year in range(1800,2025):
    if year %100==0:
        f.write(str(year)+"\n")