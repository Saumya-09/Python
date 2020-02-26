def faci(x):
    if x==1:
        return 1
    else:
        return(x*faci(x-1))
if __name__=='__main__':
    x=int(input())
    print(faci(x))