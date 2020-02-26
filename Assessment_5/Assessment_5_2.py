def patterns(n):
    a=n
    if n>0:
        for i in range(1, a + 1):
            print(i, end=' ')
            n-=1
        patterns(n)
x=int(input())
patterns(x)