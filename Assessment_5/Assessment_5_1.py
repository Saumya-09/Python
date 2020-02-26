def patterns(n):
    if n>0:
        print("*", end=' ')
        n-=1
        patterns(n)
x=int(input())
patterns(x)