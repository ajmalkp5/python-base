# remove both side object

company=("\n1234\n")
print(company.strip("\n"))

company=("v1234vjj")
print(company.strip("v"))

# remove left side object

company=("vhello 1")
print(company.lstrip("v"))

# remove right side object


company=("1 hellov")
print(company.rstrip("v"))

