def pat(x):
    for i in range(0,x):
        for j in range(0,x):
            print(j+1,end=" ")
        print(end="\n")
if __name__=='__main__':
    x = int(input())
    pat(x)