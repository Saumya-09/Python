def addition_in(x):
    num=0
    for i in x:
        a=int(x)%10
        num=num+a
        x=int(x)/10
    print(num)

if __name__=='__main__':
    x=input()
    addition_in(x)