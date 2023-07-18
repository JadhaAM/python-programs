f = open("kajal.txt")
f.seek(11)
print(f.tell())         # ask where is te file pointer
print(f.readline())     #print one line
#print(f.tell())
f.seek(0)               #reset the file pointer
print(f.readline())
#print(f.tell())
f.close()

#open file with (with block)
with open("kajal.txt") as f:
    a = f.readlines()
    print(a)

"""file is automatically closed when we open with
with block"""