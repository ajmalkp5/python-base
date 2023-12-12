from json import load
f=open("C:\\Users\\ASUS\\Desktop\\my python\\json_work\\students.json")
data=load(f)
all_names=[emp.get("name") for emp in data]

print(all_names)

depatment=[emp.get("department") for emp in data]
print(depatment)

max_sal=max(data,key=lambda d:d.get("salary"))
print(max_sal)
