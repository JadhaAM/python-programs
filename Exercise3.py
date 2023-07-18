
"""Design a calculator which will correctly solve all problems except the following once:
   45 * 3=555, 56+9=77, 56/6=4
   your program should take operator and the two numbers as input from the user and then return the result: """

# Faulty calculator
# print("This is faulty calculator.. ")
# while(True):
#  a = input("\nenter your operator which operation you perform: \n")
#  b = int(input("enter the first number: "))
#  c = int(input("enter the second number: "))
#  if a=="+":
#      if b==56 and c==9:
#          print("The addition is: 77")
#      else:
#          print("The addition is: ", b+c)
#          #exit()
#
#  if a=="-":
#      print("The substraction is: ", b-c)
#      #exit()
#
#  if a=="*":
#      if b==45 and c==3:
#          print("The multiplication is: 555")
#      else:
#          print("The multiplication is:",b*c)
#         # exit()
#
#  if a=="/":
#      if b==56 and c==6:
#          print("The division is: 4")
#      else:
#          print("The division is: ", b/c)
#          #exit()
#
#  if a=="**":
#     print("The power is: ", b**c)
#     #exit()
#
#  print("\nDo you want to use calculator again...??")
#  D=input("Press Y for yes nd N for no: ")
#  if D =="Y":
#      continue
#  if D =="N":
#      break

#this is my code
print("Faulty calculator!!")
while(True):
    m = input("Enter the operator: ")
    n = int(input("Enter the 1st num: "))
    o = int(input("Enter the 2nd num: "))

    if m=="+":
        if n==23 and o==12:
            print("the addition is: 34")
        else:
            print("the addition is: ", n+o)


    if m=="-":
        if n==56 and o==40:
            print("the substraction is: 12")
        else:
            print("the substraction is: ", n-o)

    if m=="*":
        if n==4 and o==7:
            print("the multiplication is: 78")
        else:
            print("the multiplication is: ",n*o)

    if m=="/":
        print("the division is: ", n/o)

    if m=="**":
        print("the answer is:", n**o)

    print("Do you want calculate again..??")
    k=input("Y for yes & N for no: ")
    if k=="Y":
      continue
    else:
        print("Thanks for using this calculator..!")
        break

