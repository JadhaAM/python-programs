#program to print the largest & smallst amoung the three numbers

number1=int(input("enetr the first number: "));
number2=int(input("enter the second number: "));
number3=int(input("enter the third number: "));

#code to check largest number

if number1>number2 and number1>number3:
    print("first number is largest");
if number2>number1 and number2>number3:
    print("second number is largest");
if number3>number2 and number3>number1:
    print("third number is largest"); 

#code to check smallest number

if number1<number2 and number1<number3:
    print("first number is smallest");
if number2<number1 and number2<number3:
    print("second number is smallest");
if number3<number2 and number3<number1:
    print("third number is smallest");
  