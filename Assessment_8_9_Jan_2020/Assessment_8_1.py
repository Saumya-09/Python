class Demo:
    value='Outside methods'
    def __init__(self, no1, no2):
        self.no1=no1
        self.no2=no2
    def Fun(self):
        value = 'Inside methods'
        print("From method Fun", self.value)
        print("From method Fun",self.no1)
        print("From method Fun",self.no2)
    def Gun(self):
        value = 'Inside methods'
        print("From method Fun", self.value)
        print("From method Gun",self.no1)
        print("From method Gun",self.no2)

if __name__=="__main__":
    x=int(input("Enter the 1st Number: "))
    y=int(input("Enter the 2nd Number: "))
    Obj = Demo(x,y)
    print(Obj.value)
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()