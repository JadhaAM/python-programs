#python to add natural numbers upto sum = 1+2+3+...+n

n=int(input("enter n: "))

#initalize sum & counter
sum = 0
i = 1

while i <= n:
    sum = sum+i
    i = i+1      #update counter

    print("the sum is", sum)