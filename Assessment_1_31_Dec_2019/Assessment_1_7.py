def ChkNum(number):
    if(number%5==0):
        print("True")
    else:
        print("False")
if __name__=='__main__':
    a=int(input("Enter the number "))
    ChkNum(a)