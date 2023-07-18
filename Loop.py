"""list = [ ["kajal", 4], ["Amol", 18], ["Arati", 14], ["Ravina", 12], ["Ruruja", 5], ["Sagar", 25]]
dict = dict(list)
print(dict)
for item,age in list:
    print(item,age)"""
# for loop
"""list1 = ["kajal", 8, "Namrata", 5, 6,7,9,3,2,78,14,43,"Raj","Rupa",45,76, int, float]
for item in list1:
    if type(item)==int and item>=6:          #we also used----> (if str(item).isnumeric() and item>6)
        print(item)
print()

# while loop
print("enter the current year")
i=int(input())
while(i<2030):
    i = i+1
    print("the years till 2030 are", i)"""

while(True):
    i= int(input("Enter a number: \n"))
    if i>100:
        print("Congrats you have entered a number greater than 100")
        break
    else:
        print("Try again...!\n")
        continue
# OR
while(1):
    m=float(input("Enter the number: "))
    if m>100:
        print("Congrats! u hve enterd a no greater than 100")
        break
    else:
        print("Try again..")

# OR
while int(input("enter a num: \n"))<100:
    print("Try again..")
print("good..")