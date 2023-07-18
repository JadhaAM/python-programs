#program to demonstrate else with for

for i in range(0,5):
    print(i)

else:
    print("for loop completely exhausted, since there is no break.");

    print("out of loop")

#program to demonstrate else with for & break

for i in range(0,5):
    print(i<4)
    break

else:
    print("for loop completely exhausted, since there is no break.");
    print("out of loop")