def ChkNum():
    num=int(input("Enter the number "))
    if num>0:
        print("Positive Number")
    elif num<0:
        print("Negative Number")
    else:
        print("Zero")
if __name__=='__main__':
    ChkNum()