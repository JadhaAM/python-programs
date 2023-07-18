def recur_fun(n):
    if n<=1:
        return n
    else:
        return (recur_fun(n-1) + recur_fun(n-2))

nterm = int(input("enter the number what you want? "))
if nterm <= 0:
    print("Please enter positive number...")
else:
    print("Fibonacci sequence: ")
    for i in range(nterm):
        print(recur_fun(i))