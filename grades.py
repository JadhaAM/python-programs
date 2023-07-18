#program to display the grades as A+, A, B+, B, C+, C and fail from marks

marks=int(input("enter the marks..?"))

if marks>90 and marks<=100:
    print("congrats ! you scored grade A+...")
elif marks>80 and marks <= 90:
    print("congrats ! you scored grade A...")
elif marks>70 and marks<= 80:
    print("you scored grade B+...")
elif marks>60 and marks<= 70:
    print("you scored grade B...")
elif marks>50 and marks<= 60:
    print("you scored grade C+...")
elif marks>40 and marks<= 50:
    print("you scored grade C...")

else:
    print("sorry you are fail...")