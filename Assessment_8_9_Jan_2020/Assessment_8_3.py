class Arithmetic:
    def __init__(self, Value1,Value2):
        self.Value1 = Value1
        self.Value2 = Value2
    def Accept(self):
        self.Value1 = int(input("Enter the 1st Value: "))
        self.Value2 = int(input("Enter the 2nd Value: "))
    def Addition(self):
        self.Add = self.Value1 + self.Value2
        return self.Add
    def Substraction(self):
        self.Sub = self.Value1 - self.Value2
        return self.Sub
    def Multiplication(self):
        self.Mul = self.Value1 * self.Value2
        return self.Mul
    def Division(self):
        self.Div = self.Value1 / self.Value2
        return self.Div



if __name__=="__main__":
    Obj1 = Arithmetic(0.0,0.0)
    Obj1.Accept()
    print("The Addition is: ",Obj1.Addition())
    print("The Substraction is: ",Obj1.Substraction())
    print("The Multiplication is: ",Obj1.Multiplication())
    print("The Division is: ",Obj1.Division())

    Obj2 = Arithmetic(0.0, 0.0)
    Obj2.Accept()
    print("The Addition is: ",Obj2.Addition())
    print("The Substraction is: ",Obj2.Substraction())
    print("The Multiplication is: ",Obj2.Multiplication())
    print("The Division is: ",Obj2.Division())
