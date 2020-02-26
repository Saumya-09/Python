def Ser(n):
    l1=[]
    for i in range(0,n):
        x = int(input())
        l1.append(x)
    print(l1)
    y = int(input("Element to be Searched: "))
    c=l1.count(y)
    return c
z=int(input("Input number of Elements: "))
print(Ser(z))