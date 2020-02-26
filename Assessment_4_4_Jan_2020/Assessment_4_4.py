def Delete_string(Str,posi):
    l=list(Str)
    print(l)
    for i in l:
        if i==posi:
            l.delete(i)
    print(l)
x=input()
y=int(input())
Delete_string(x,y)
