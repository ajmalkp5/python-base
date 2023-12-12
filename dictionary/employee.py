employee={"id":100,"name":"ajmal","department":"developer","salary":50000}

employee["department"]="seniordeveloper"
print(employee)

#if salary not present add salary as 50000 else add bonous od 10000

if "salary" not in employee:
    employee["salary"]=50000

else:
    employee["salary"]+=10000

print(employee)
