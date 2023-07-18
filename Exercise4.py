"""no=18
 no of guesses 9
print no of guesses left
no of guesses he took to finish
me.over"""
a =1
while(True):
    b = int(input("enter a number: "))
    if b>18:
        print("decrease the number..")
    elif b==18:
        print("Congrats! you won...!")
        break

    elif b<18:
        print("increase the number..")

    print(a, "chances endup..\n")
    a+=1
    if a>9:
        print("Game over!!")
        break

  # OR
n=18
no_of_guesses=1
print("\n \nnumber of guesses is limited to only 9 guesses\n")
while (no_of_guesses<=9):
    num = int(input("Guess the number: \n"))
    if num<18:
        print("You entered small number plz enter greater number..\n")
    elif num>18:
        print("You entered greater number plz enter small number..\n")
    else:
        print("Congrats! you won")
        print(no_of_guesses,"no of guesses he took to finish")
        break

    print(no_of_guesses,"number of guesses left ")
    no_of_guesses+= 1

    if (no_of_guesses>9):
        print("Game over")
        break