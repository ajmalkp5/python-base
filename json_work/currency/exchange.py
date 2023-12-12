from json import load

f=open("C:\\Users\\ASUS\\Desktop\\my python\\json_work\\currency\\data.json",encoding="utf-8")
data=load(f)

source_currency_code=input("enter source currency code")
target_currency_code=input("enter destination currency code")

amount=int(input("enter amount"))

conversion_rates=data.get("conversion_rates")

source_currency_code_rate=conversion_rates.get(source_currency_code)
destination_currency_rate=conversion_rates.get(target_currency_code)

print(source_currency_code_rate)
print(destination_currency_rate)
print(conversion_rates)

# res=(amount/source_currency_code_rate)*destination_currency_rate
# print(res)