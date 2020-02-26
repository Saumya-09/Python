def Maxi(n):
    l1=[]
    for i in range(0,n):
        x = int(input())
        l1.append(x)
    s=max(l1)
    print(l1)
    return s
z=int(input("Input number of Elements: "))
print(Maxi(z))