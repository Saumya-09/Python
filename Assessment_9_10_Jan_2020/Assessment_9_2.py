class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display (self):
        print(self.Name)
        print(self.Amount)

    def Deposite (self, value):
        self.value=value
        self.Amount = self.Amount+self.value

    def Withdraw (self, val):
        self.val = val
        self.Amount = self.Amount - self.val

    def CalculateInterest (self):
        Interest = self.ROI*self.Amount
        return Interest

if __name__=='__main__':
    obj1 = BankAccount("Saumya bhatt",10000)
    obj1.Display()
    obj1.Deposite(100)
    obj1.Withdraw(50)
    print("Interest is: ",obj1.CalculateInterest())
    obj1.Display()

    obj2 = BankAccount("Deepak Bhavsar",5000)
    obj2.Display()
    obj2.Deposite(100)
    obj2.Withdraw(50)
    print("Interest is: ",obj2.CalculateInterest())
    obj2.Display()