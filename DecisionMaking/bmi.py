weight_inkg=int(input("enter wight in kg"))

heightin_cm=int(input("enter height in cm"))

heightin_meter=heightin_cm/100

bmi=weight_inkg/heightin_meter**2
print(bmi)


# bmi<19=underweight
# 19-25=healthy
# 25-30=overweight
# 30-40=obesity
# >40= severe obese

if bmi<19:
    print("under weight")
elif bmi<25:
    print("healthy")
elif bmi<30:
    print("overweight")
elif bmi<40:
    print("obesity")
else:
    print("severe obese")        
