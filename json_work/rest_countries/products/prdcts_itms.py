from json import load
f=open("C:\\Users\\ASUS\\Desktop\\my python\\json_work\\rest_countries\\products\\items.json",encoding="utf-8")
data=load(f)
print(len(data))

catogery={p.get ("category")for p in data}
print(catogery)

electronics_product=[p for p in data if p.get("category")=="electronics"]
print(len(electronics_product))