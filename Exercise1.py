print("***** wlcome to my dictonary *****")
dictonary = {"Afar":"Far off or away", "Fool":"Silly or stupid", "Famous":"popular",
             "Abase":"cause to feel shame","benefit":"advantage","Endear":"make attractive",
             "Array":"collection of similar data types","Protocol":"set of rules", "Data":"collection of information",
             "Abstraction":"set of function, domain & axoms", "Software":"collection of programs"}
print("Enter the word which you have meaning: ")
Search=input()
s = Search.capitalize()
print(s, "=" , dictonary[s])
print("Thanks for using my dictonary....!!!")