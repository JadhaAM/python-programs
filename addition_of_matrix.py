row_num=int(input("enter the number of rows:"))
col_num=int(input("enter the number of cols:"))
arr1=[[0 for col in range (col_num)]for row in range (row_num)]
for row in range(row_num):
    for col in range(col_num):
        item=int(input("enter the element:"))
        arr1[row][col]=item
print("the first matrix is:")
for r in arr1:
    print(r)

arr2=[[0 for col in range(col_num)]for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        item=int(input("enter the element:"))
        arr2[row][col]=item
print("the second matrix is:")
for r in arr2:
    print(r)

result=[[arr1[row][col] + arr2[row][col]for col in range(len(arr2[0]))]for row in range(len(arr2))]
print("addition of two matrix:")
for r in result:
    print(r)