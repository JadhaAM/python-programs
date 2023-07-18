# a = 5
# b= 45
# c = sum((a,b))     #built in function
# print(c)
#
# def fun1(a,b):                 #user defined function
#     print("hello..!! Pycharm",  a+b)
# fun1(3, 8)
#
# def fun2(a,b):
#     """This is function which will calculate average of two numbers"""  """" <-- this is doc string"""
#     ave = (a+b)/2
#     #print(ave)
#     return ave     # optional but important
#
# v = fun2(5,7)      # value of ave store in variable v
# print(v)
# print(fun2.__doc__)
#
# # Try_except handling:
#
# print("\n\nEnter 1st num:")
# num1=input()
# print("enter 2nd num:")
# num2=input()
# try:                                  # Handle the error & print next statement
#     print("The sum of two numbers:", int(num1)+int(num2))
# except Exception as e:
#     print(e)
#
# print("My name is kajal..")

# Quetion :-
def function1(m,n):
    """this is the doc string"""   """  #for read the doc string"""
    mul=m*n
    print("the multiplication is:", mul)
function1(4,5)
print(function1.__doc__)    #for print the doc string


