# pattern priting
n = int(input("Enter how many rows you want:"))
m = int(input("Enter 0 or 1:"))
j = bool(m)
k = 0
while k<=n:
    if j==True:
        print("*"*k)

    if j==False:
        print("*"*(n-k))
    k=k+1

# OR
a = int(input("Enter the rows you want:\n"))
b = int(input("Enter 0 or 1: "))
c=bool(b)
if c== True:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*", end="")
        print()
elif c==False:
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()

#using Try and Catch method
try:
    n = int(input("Enter of rows: "))
    b = int(input("enter the pattern(0 or 1) : "))
    if b==0:
        count = 0
        while(count<=n):
            print("*"* count, end="")
            print("\n", end="")
            count = count + 1
    elif b==1:
        count = n
        while(count !=0):
            print("*"* count, end="")
            print("\n", end="")
            count = count - 1
    else:
        print("Invalid Pattern.....")

except Exception as e:
    print("Invalid Input.....")
