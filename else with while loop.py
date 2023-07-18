#program to demonstrate else with while

i=0
while i<5:
    print(i)
    i=i+1

else:
    print("while loop completely exhausted, since there is no break.");
print("out of loop")

#program to demostrate else with while & break
i=0
while i<6:
    print(i)
    i=i+1
    break

else:
    print("while loop completely exhausted, since there is no break.");
print("out of loop")