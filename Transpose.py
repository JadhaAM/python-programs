
R = int(input("Enter the number of Rows: "))
C = int(input("Enter the number of columns: "))

matrix = []
print("Enter the entries row wise: ")


for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

    result = []
print("Transposition of matrix: ")
for j in range(R):
    for i in range(C):
        print(matrix[i][j],end=" ")
    print()