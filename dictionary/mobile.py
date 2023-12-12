mobile={"id":100,"name":"iphone15","price":100000,"imei":2345,"proccesor":"ios"}

#print all key values

for k,v in mobile.items():
    print(k,v)

#print name

print(mobile.get("name"))

#update price as rs 85000

mobile["price"]=85000

#remove imei

mobile.pop("imei")
print(mobile)

#update a key 

mobile.update({"offer":1000})
print(mobile)
#another way
mobile["offer"]=1000

#add or substract or * or / into keys

mobile["price"]-=1000
mobile["offer"]+=100
print(mobile)

#for searching key  or values true or false

print("color" in mobile)