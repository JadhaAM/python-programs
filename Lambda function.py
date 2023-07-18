#lambda functions only for convenious
# lambda function or anonymous function
# def add(a,b):
#     return  a+b
#
# #minus = lambda x, y: x-y
#
# def minus(x,y):
#     return  x-y
# print(minus(9,4))
def a_first(a):
    return a[1]
a = [[1,7], [5,9], [4,24]]
a.sort(key=a_first)             #key is argument give function as input
print(a)