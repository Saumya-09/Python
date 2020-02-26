def patterns(n):
    if n>0:
        print(n, end=' ')
        n-=1
        patterns(n)
x=int(input())
patterns(x)