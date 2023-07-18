n = int(input("enter number of rows needed:"))
for i in range(n):
    for j in range(i + 1):  # for number pyramid
        print(j + 1, end=" ")
    print()

for i in range(n):
    for j in range(i, -1, -1):  # for reverse number pyramid
        print(j + 1, end=" ")
    print()

for i in range(n):
    for j in range(i, -1, -1):  # for repeat 1 22 333 in pyramid
        print(i + 1, end=" ")
    print()

for i in range(n):
    for j in range(i + 1):
        print(n - i, end=" ")  # for repeat 3 22 111 in pyramid
    print()

for i in range(n):
    for j in range(i + 1):
        print(n - j, end=" ")  # for reverse 3 32 321 pyramid
    print()

for i in range(n):
    for j in range(i, -1, -1):
        print(n - j, end=" ")  # for 3 23 123 pyramid
    print()

for i in range(n):
    for i in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i, -1, -1):
        print(n - j, end=" ")
    print()