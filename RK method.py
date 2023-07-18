# RK method

def f(x,y):
    return x*y+y**2
y1 = 0
x0 = float(input("Enter the initial approximation x0 = "))
y0 = float(input("Enter the initial approximation y0 = "))
h = float(input("Enter the step size, h= "))
x1 = float(input("Enter the value for which answer to be find out x1= "))
n = int(input("Enter the number of iteration n= "))
count = 1
while (count <= n):
    k1 = h*f(x0, y0)
    k2 = h*f((x0+h/2), (y0+k1/2))
    k3 = h*f((x0+h/2), (y0+k2/2))
    k4 = h*f((x0+h), (y0+k3))
    y1 = y0+(1/6)*(k1+2*k2+2*k3+k4)

print("Iteration: ", count)
print("The new value of y is ", y1)
   x1 = h+x0
   x0 =x1
   y0 = y1
   count = count +1