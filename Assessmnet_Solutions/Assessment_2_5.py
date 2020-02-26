def Chkprime(n):
    for i in range(2,n):
        if n%i==0:
            return ("Not Prime")
        else:
            return ("Prime")
x=int(input())
print(Chkprime(x))