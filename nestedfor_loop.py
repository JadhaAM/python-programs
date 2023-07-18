#program to demonstrate nested for loop

rows = int(input("enter the "))
i,j=0,0

for i in range(0,rows):
    print()
    for j in range (0,i+1):
        print("$", end="") 
        

# easy code for numbers in pyramid shape
a="2345"
b=""
for num in a:
    b=b+num
    print(b)