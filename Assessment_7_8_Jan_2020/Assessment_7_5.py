from functools import reduce
class Filter_Map_Reduce():
    l=[]
    f=[]
    m=[]
    re=[]
    n=int(input("Enter the number of elements needed: "))
    for i in range(0,n):
        lis=int(input("Enter the number: "))
        l.append(lis)
    for i in l:
        for j in range(2,i):
            if i%j==0:
                f.append(i)
    print("List after Filter: ",f)
    m = list(map(lambda x: (x*2), f))
    print("List after Map: ", m)
    re = reduce(lambda x, y: (max(x,y)), m)
    print("List after Reduce",re)

if __name__=='__main__':
    p=Filter_Map_Reduce()