
# # decerators

# def swap_num(fn):
#     def wrapper(n1,n2):
#         if n1<n2:
#             (n1,n2)=(n2,n1)
#         return fn(n1,n2)
#     return wrapper

# @swap_num
# def sub(n1,n2):
    
#     return n1-n2

# @swap_num
# def div(n1,n2):
    
#     return (n1/n2)

# print(sub(2,10))
# print(div(2,10))

# ---------------------------------------------------------------------------------------------

# def hello_decorator(fn):

#     def wrapper(user):
#         data="hello !"+fn(user)
#         return data
#     return wrapper

# @hello_decorator
# def morning_greeting(user):

#     return f"good morning {user}"

# @hello_decorator
# def afternoon_greeting(user):

#     return f"good afternoon {user}"

# @hello_decorator
# def evening_greeting(user):

#     return f"good evening {user}"

# print(morning_greeting("hari"))
# print(afternoon_greeting("hari"))
# print(evening_greeting("hari"))

# ---------------------------------------------------------------------------------------


def get_decorator(fn):

    def wrapper():
        data=f"<b>{fn()}</b>"
        return data
    return wrapper


@get_decorator
def get_hello():
    return "hello"


@get_decorator
def get_hai():
    return "hai"

print(get_hello())
print(get_hai())