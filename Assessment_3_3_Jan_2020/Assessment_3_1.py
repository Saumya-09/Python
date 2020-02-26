def Addi(n):
    l1=[]
    sum=0
    for i in range(0,n):
        x=int(input())
        sum += x
        l1.append(x)
    print(l1)
    return sum
z=int(input("Input number of Elements: "))
print(Addi(z))