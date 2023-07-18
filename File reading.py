# File to basics
"""
"r" - Open file for reading --- default
"w" - open a file for writing
"x" - creates file if not exists
"a" - Add more content to a file
"t" - Text mode ---default
"b" - Binary mode
"+" - Read and write
"""
f= open("kajal.txt", "rt")
print(f.readlines())   #print lines in list
# print(f.readline())    #print only one line
# print((f.readline()))
# content = f.read()
# for line in content :
#     print(line)     #print sentence character by character

# for line in f:
#     print(line, end="")
# content = f.read(3445)
# print("1", content)
#
# content = f.read(3445)
# print("2", content)
f.close()
