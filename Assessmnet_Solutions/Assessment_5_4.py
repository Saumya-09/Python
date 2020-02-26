def rec(x):
    if x>0:
        n=x//10
        temp=(x%10)+rec(n)
    else:
        return 0
    return temp
x=int(input())
print(rec(x))