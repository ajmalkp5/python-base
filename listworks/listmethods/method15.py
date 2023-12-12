# list comprehsion

# upper case
c4=["ajmal","suhail","prashanth","manoj","anshad"]
upper_names=[name.upper() for name in c4 ]
print(upper_names)

# print names whose length>5
name_gt_5=[name for name in c4 if len(name)>5]
print(name_gt_5)

