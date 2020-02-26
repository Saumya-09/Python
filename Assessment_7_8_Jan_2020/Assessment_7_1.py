class Power():
    # def __init__(self):(self,number):
    #     self.number=number
    number = int(input("Enter the number: "))
    f=lambda number : number**2
    print(f(number))
if __name__=='__main__':
    p=Power()