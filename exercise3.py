name, char= input("enter comma sepereted name and character : ").split(",")
print(f"lenght of your name: {len(name)}")
print(f"count of character is: {name.count(char)}")  #case sensitive
print(f"count character: {name.lower().count(char.lower())}")  #case insensitive
# Kajal - kajal
#  K - k
#name.lower().count(char.lower())
#char.lower()

print(f"count of character is: {name.strip().lower().count(char.strip().lower())}")