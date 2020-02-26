from functools import reduce
class Multiplication():
    l=[]
    for i in range(0,2):
        lis=int(input("Enter the number: "))
        l.append(lis)

    f = reduce(lambda x,y: (x*y),l)
    print(f)
if __name__=='__main__':
    p=Multiplication()