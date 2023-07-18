#using iterative method
def factorial_iterative(n):
    """
    :param n: integer
    :return :  n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


#using recursion
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    pass
number = int(input("Enter then number: "))
print("factorial using iterative method", factorial_iterative(number))
print("factorial using iterative method", factorial_recursive(number))
