# args=* 

# def add_numbers(*args):
#     return sum(args)

# print(add_numbers(10,20))
# print(add_numbers(10,20,20,20))
# print(add_numbers(10,21,2,3,4,3))


# last digit sum

# def last_dgt_sum(*args):

#     digits=[n%10 for n in args]
#     return sum(digits)

# ----------------------------------------------------------------------------------------

# maximum digit

# def last_dgt_sum(*args):

#     digits=[n%10 for n in args]
#     return max(digits)

# print(last_dgt_sum(123,45,67,86))




# kwargs=**

# def add_employee(**kwargs):
#     print(kwargs.get("name"))
#     print(kwargs.get("w_place"))


# add_employee(id=20,name="manu",n_place="ernklm",w_place="bnglr",salary="20000")


# *args,**kwargs


def last_dgt_sort(*args,**kwargs):

    digits=[n%10 for n in args]
    value=kwargs.get("reversed")
    if value==True:
        digits.sort(reverse=True)
    else:
        digits.sort()
    return digits


print(last_dgt_sort(17,12,14,3,1,reversed=False))
print(last_dgt_sort(17,12,14,3,1,reversed=True))





