def Count_Words(Str):
    l=list(Str)
    x=1
    for i in l:
        if i==' ':
            x+=1
    return(x)

x=input()
print(Count_Words(x))