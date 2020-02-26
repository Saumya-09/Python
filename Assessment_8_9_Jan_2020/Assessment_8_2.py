class Circle:
    PI = 3.14
    def __init__(self, Radius, Area, Circumference):
        self.Radius = Radius
        self.Area = Area
        self.Circumference = Circumference
    def Accept(self):
        self.Radius=float(input("Enter the Radius: "))
    def CalculateArea(self):
        self.Area=self.PI*(self.Radius**2)
    def CalculateCircumference(self):
        self.Circumference=2*self.PI*self.Radius
    def Display(self):
        print("Radius of the Circle is: ",self.Radius)
        print("Area of the Circle is: ", self.Area)
        print("Circumference of the Circle is: ", self.Circumference)



if __name__=="__main__":
    Obj1 = Circle(0.0,0.0,0.0)
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()
    Obj2 = Circle(0.0,0.0,0.0)
    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()