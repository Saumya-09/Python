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
    print("Input list: ",l)
    f = list(filter(lambda x : (x>=70 and x<=90),l))
    print("List after Filter: ",f)
    m = list(map(lambda x: (x+10), f))
    print("List after Filter: ", m)
    re = reduce(lambda x, y: (x * y), m)
    print("List after Reduce",re)

if __name__=='__main__':
    p=Filter_Map_Reduce()