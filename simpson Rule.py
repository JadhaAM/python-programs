# Simpson 1/3 Rule
def f(x):
    return 1/(1+x**2)

def simpson13(x0, xn, n):
    h = (xn - x0) / n

    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i*h

        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    integration = integration * h/3

    return integration

x0 = float(input("enter lower limit of integration, x0: "))
xn = float(input("enter upper limit of integration, xn: "))
n = int(input("Enter number of sub intervals, n: "))

result = simpson13(x0,xn,n)
print("Integration result by Simpson's 1/3 method is: %0.6f" %(result))