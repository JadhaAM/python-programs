l = 15    # Global --- use anywhere (sarkar ka rupya)

def function1 (n):
   # l = 5   # local --- only use in function (khud ka rupya)
    m = 7  #local
    global l     #(by declaring global scope we change the value of l)
    l = l + 24   #(we cannot change l when it is not defimed in locally )
    print(l, m, )   # 1st check in local & then Global
    print(n, "I have printed")

function1("This is me")
print(l)   #print Global scope

x=56
def kajal():
    x = 30
    def Arati():
        global x
        x=69

    print("Before calling Arati()", x)
    Arati()
    print("After calling Arati()", x)

kajal()
print(x)   #print 69 because  we change global variable from 56 to 69