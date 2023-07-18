nterm = int(input("enter the number what you want?  "))

n1, n2 =0, 1
count = 0
if nterm <=0:
    print("Please enter the Positive number")
elif nterm == 1:
    print("fabanacci series upto", nterm, ":")
    print(n1)
else:
    while count < nterm:
        print(n1)
        nth = n1+n2

        n1 = n2
        n2 = nth
        count += 1