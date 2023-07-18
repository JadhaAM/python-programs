n=int(input("how many elements are there in array?"))
array=[]
i=0
for i in range(n):
    ele=int(input("enter the elements in array: "))
    array.append(ele)
print(array)

pos=int(input("enter the position where you want to the element: ")) 
value=int(input("enter the element you want"))
array=array[:pos] + [value] + array[pos:]
print(array)