from json import load

f=open("C:\\Users\\ASUS\\Desktop\\my python\\json_work\\rest_countries\\data.json",encoding="utf-8")

data=load(f)
print(len(data))

# all country names

all_country_name=[c.get ("name") for c in data]
# print(all_country_name)

# independent country names

independent_cntry=[c.get("name") for c in data if c.get("independent")==True]
# print(independent_cntry)

# all regions

all_regions={c.get("region") for c in data}
# print(all_regions)


# asian country names

asian_countries=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_countries)

# print capital of ukraine

capital_ukraine=[c.get("capital")for c in data if c.get("name")=="Ukraine"]
# print(capital_ukraine)

# print capital of india

india_capital=[c.get("capital")for c in data if c.get("name")=="India"]
# print(india_capital)

# countryname capital
countries_capital={(c.get("name"),c.get("capital")) for c in data}
# print(countries_capital)

# print country name and currency name
# difficult way
# for c in data:
#     if "currencies" in c:
#         currency_data=c.get("currencies")[0]
#         print(currency_data.get("name"),",",("names"))

    # break

# simple way

# indian borders

indian_borders=[c.get("borders")for c in data if c.get("name")=="India"][0]
# print(indian_borders)

# indian border names
indian_borders=[c.get("borders")for c in data if c.get("name")=="India"][0]
indian_border_nmaes=[c.get("name")for c in data if c.get("alpha3Code") in indian_borders]
print(indian_border_nmaes)
# above 4 borders country
for c in data:
    if "borders" in c and len(c.get("borders"))>4:
        print(c.get("name"))