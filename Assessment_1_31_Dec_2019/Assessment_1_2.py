def ChkNum(number):
    if(number%2==0):
        print("Even number")
    else:
        print("Odd number")

if __name__=='__main__':
    a=int(input("Enter the number "))
    ChkNum(a)