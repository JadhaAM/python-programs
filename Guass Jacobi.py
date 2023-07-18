# Gauss Seidal Method

def f(x,y,z):
    return (1/27)*(85-6*y+z)

def g(x,y,z):
    return (1/15)*(72-6*x-2*z)

def h(x,y,z):
    return (1/54)*(110-x-y)

x0 = float(input("Enter the initial approximation x0= "))
y0 = float(input("Enter the initial approximation y0= "))
z0 = float(input("Enter the initial approximation z0= "))

n= int(input("Enter the number of iteration n= "))
count = 1
while (count):
    x= f(x0, y0, z0)
    y= g(x0, y0, z0)
    z= h(x0, y0, z0)

    x0 = x
    y0 = y
    z0 = z

print("Iteration: ", count)
print("The new value of x is ", x)
print("The new value of y is ",y)
print("The new value of z is ", z)
count = count + 1