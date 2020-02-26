def addi(n):
    str1=str(n)
    l=len(str1)
    for i in range(1,l+1):
        a=n%10
        temp+=a
        n=n/10
    addi(l-1)
    return temp
x=int(input())
print(addi(x))