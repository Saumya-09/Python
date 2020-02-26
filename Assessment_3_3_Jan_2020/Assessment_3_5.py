from MarvellousNum_3_5 import *
def ListPrime(n):
    l1=[]
    for i in range(1,n+1):
        x = int(input())
        l1.append(x)
    print(l1)
    for i in range(1,n+1):
        print(ChkPrime(i))
z=int(input("Input number of Elements: "))
ListPrime(z)