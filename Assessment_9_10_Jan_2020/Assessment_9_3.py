class Numbers:


    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        for i in range(2,self.Value):
            if self.Value%i==0:
                return ("false")
            else:
                return ("true")

    def ChkPerfect(self):
        temp = 0
        for i in range(1, self.Value-1):
            if self.Value % i == 0:
                temp += i
            else:
                continue
        if temp == self.Value:
            print("perfect: true")
        else:
            print("perfect: false")

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
            else:
                continue
        return sum

    def Factors(self):
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i)
            else:
                continue


if __name__ == '__main__':
    obj1 = Numbers(6)
    obj1.ChkPrime()
    obj1.ChkPerfect()
    obj1.Factors()
    print("Sum: ",obj1.SumFactors())
