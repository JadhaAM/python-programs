f = open("kajal.txt", "w")
a = f.write("my name is gauri\n")
print(a)
f.close()

f = open("kajal.txt", "a")
a = f.write("my name is gauri\n")
print(a)
f.close()

# Handle read and write both
f = open("kajal.txt", "r+")
print(f.read())
f.write("Thank you")
f.close()
