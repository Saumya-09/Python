# Nested Classes
### Introduction
A nested or inner class is contained within another class. This could be for reasons of encapsulation, where the inner class is not useful by itself.

Here is an example of how the classes are laid out.

```python
class A:
    class B:
        pass
    pass
```
An inner class in python is a distinct entity in that it does not automatically get access to the outer class members in any special way.

Example:
```python
class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
    
class Head:
    def talk(self):
        return 'talking...'
    
    if __name__ == '__main__':
        guido = Human()
        print guido.name
        print guido.head.talk()

Output:

Guido
talking...
```

### Class :
Class is a set or category of things having some property or attribute in common and differentiated from others by kind, type, or quality.

In technical terms we can say that class is a blue print for individual objects with exact behaviour.

### Object :
object is one of instances of the class. which can perform the functionalities which are defined in the class.

### self :
self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.

### __init__ :
" __init__  is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.

> class class_name(object):
  ""
    blueprint for class
  ""

 ```python
 def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating...")
    "accelarator functionality here"

  def change_gear(self, gear_type):
    print("gear changed")
    " gear related functionality here"
```
> maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

We have created two different types of car objects with the same class. while creating the car object we passed arguments  "ertiga", "black", "suzuki", 60  these arguments will pass to "__init__" method  to initialize the object. 

The self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python. It binds the attributes with the given arguments. The reason why we use self is that Python does not use the ‘@’ syntax to refer to instance attributes. In Python, we have methods that make the instance to be passed automatically, but not received automatically.

# What are objects in Python?
Python is an object oriented programming language. Unlike procedure oriented programming, where the main emphasis is on functions, object oriented programming stress on objects.

Object is simply a collection of data (variables) and methods (functions) that act on those data. And, class is a blueprint for the object.

As, many houses can be made from a description, we can create many objects from a class. An object is also called an instance of a class and the process of creating this object is called instantiation.

### Creating an Object in Python
We saw that the class object could be used to access different attributes.

It can also be used to create new object instances (instantiation) of that class. The procedure to create an object is similar to a function call.

> ob = MyClass()

This will create a new instance object named ob. We can access attributes of objects using the object name prefix.

Attributes may be data or method. Method of an object are corresponding functions of that class. Any function object that is a class attribute defines a method for objects of that class.

This means to say, since MyClass.func is a function object (attribute of class), ob.func will be a method object.

# Python Constructors
Python as a programming language follows object orientation, meaning which every instance that is created on the platform is defined as an object. Although most of the components in Python have a ton of information online, one topic that keep getting researched over and over again is that of a constructor in Python. Therefore in this article we will discuss all about constructors in Python, how you can make use of them and the benefits they bring to the table.

### What is a Constructor in Python?
A constructor can simply be defined as a special type of method or function which can be used to initialize instances of various members in a class.

In Python, there are two different types of constructors.

- Non-parameterized Constructor: The constructors in Python which have no parametres present is known as a non parameterized constructor.
- Parameterized Constructor: A constructor that has a parametre pre defined is known as a parameterized constructor.

A constructor is defined the moment we create an object inside a class. The presence of a constructor also verifies that enough resources are present, so that a start up task can easily be executed via an object of a class.

### Creating a Constructor in Python
Now that you have acquainted yourself with the definition and types of constructors in Python, let us explore how we can create a constructor in Python.

In Python, if you need to create a construct you need to make use of the __init__ function and or method. You need to call upon this method, the moment a class is instantiated. Once the __init__ function has been defined and called upon, we can pass any number of arguments at the time of creating the class objects depending upon your needs. The most common use of a constructor in Python is to initialize the attributes of a class.

### Types of Constructor:

-  Parameterized Constructor
- Non Parameterized Constructor
Difference between Parameterized and Non Parameterized Constructor
As mentioned in the definitions above, a parameterized constructor is one which has a predefined value and a non parameterized constructor is one which has no value assigned to it. While programming the use cases vary depending upon the context, and to understand this better, take a look at the examples below.

```python
class Student:
def __init__(self):
print("This is non parametrized constructor")
def show(self,name):
print("Hello",name)
student = Student()
student.show("John")

Output:

This is non parametrized constructor
Hello John
```

```python
class Student:
#Constructor - parameterized
def __init__(self, name):
print("This is parametrized constructor")
self.name = name
def show(self):
print("Hello",self.name)
student = Student("John")
student.show()

Output:
This is parametrized constructor
Hello John
```
# Abstraction:
Suppose you booked a movie ticket from bookmyshow using net banking or any other process. You do not know the procedure of how the pin is generated or how the verification is done. This is called ‘abstraction’ from the programming aspect, it basically means you only show the implementation details of a particular process and hide the details from the user. It is used to simplify complex problems by modeling classes appropriate to the problem.

An abstract class cannot be instantiated which simply means you cannot create objects for this type of class. It can only be used for inheriting the functionalities.

Example:

```python
from abc import ABC,abstractmethod
class employee(ABC):
def emp_id(self,id,name,age,salary):    //Abstraction
pass
 
class childemployee1(employee):
def emp_id(self,id):
print("emp_id is 12345")
 
emp1 = childemployee1()
emp1.emp_id(id)

Output:
emp_id is 12345
```

Explanation: As you can see in the above example, we have imported an abstract method and the rest of the program has a parent and a derived class. An object is instantiated for the ‘childemployee’ base class and functionality of abstract is being used.

This brings us to the end of our article on “Object-Oriented Programming Python”. I hope you have cleared with all the concepts related to Python class, objects and object-oriented concepts in python. Make sure you practice as much as possible and revert your experience.

# Polymorphism:

You all must have used GPS for navigating the route, Isn’t it amazing how many different routes you come across for the same destination depending on the traffic, from a programming point of view this is called ‘polymorphism’. It is one such OOP methodology where one task can be performed in several different ways. To put it in simple words, it is a property of an object which allows it to take multiple forms.

[![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/06/Polymorphism-528x146.png)](http://https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/06/Polymorphism-528x146.png)

- Compile-time Polymorphism
- Run-time Polymorphism

#### Compile-time Polymorphism:
A compile-time polymorphism also called as static polymorphism which gets resolved during the compilation time of the program. One common example is “method overloading”. Let me show you a quick example of the same.

Example:


```python
class employee1():
def name(self):
print("Harshit is his name")    
def salary(self):
print("3000 is his salary")
 
def age(self):
print("22 is his age")
 
class employee2():
def name(self):
print("Rahul is his name")
 
def salary(self):
print("4000 is his salary")
 
def age(self):
print("23 is his age")
 
def func(obj)://Method Overloading
obj.name()
obj.salary()
obj.age()
 
obj_emp1 = employee1()
obj_emp2 = employee2()
 
func(obj_emp1)
func(obj_emp2)

Output:

Harshit is his name
3000 is his salary
22 is his age
Rahul is his name
4000 is his salary
23 is his age
```

Explanation:

In the above Program, I have created two classes ’employee1′ and ’employee2′ and created functions for both ‘name’, ‘salary’ and  ‘age’ and printed the value of the same without taking it from the user.

Now, welcome to the main part where I have created a function with ‘obj’ as the parameter and calling all the three functions i.e. ‘name’, ‘age’ and ‘salary’.

Later, instantiated objects emp_1 and emp_2 against the two classes and simply called the function. Such type is called method overloading which allows a class to have more than one method under the same name.

#### Run-time Polymorphism:
A run-time Polymorphism is also, called as dynamic polymorphism where it gets resolved into the run time. One common example of Run-time polymorphism is “method overriding”. Let me show you through an example for a better understanding.

Example:

```python
class employee():
   def __init__(self,name,age,id,salary):  
       self.name = name
       self.age = age
       self.salary = salary
       self.id = id
def earn(self):
        pass
 
class childemployee1(employee):
 
   def earn(self)://Run-time polymorphism
      print("no money")
 
class childemployee2(employee):
 
   def earn(self):
       print("has money")
 
c = childemployee1
c.earn(employee)
d = childemployee2
d.earn(employee)

Output: 
no money, has money
```

Explanation: In the above example, I have created two classes ‘childemployee1’ and ‘childemployee2’ which are derived from the same base class ‘employee’.Here’s the catch one did not receive money whereas the other one gets. Now the real question is how did this happen? Well, here if you look closely I created an empty function and used Pass ( a statement which is used when you do not want to execute any command or code). Now, Under the two derived classes, I used the same empty function and made use of the print statement as ‘no money’ and ‘has money’.Lastly, created two objects and called the function.

# Inheritance:
Ever heard of this dialogue from relatives “you look exactly like your father/mother” the reason behind this is called ‘inheritance’. From the Programming aspect, It generally means “inheriting or transfer of characteristics from parent to child class without any modification”. The new class is called the derived/child class and the one from which it is derived is called a parent/base class.

[![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/07/Types-of-Inheritance.jpg)](http://https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/07/Types-of-Inheritance.jpg)

#### Single Inheritance:
Single level inheritance enables a derived class to inherit characteristics from a single parent class.

Example:

```python
class employee1()://This is a parent class
def __init__(self, name, age, salary):  
self.name = name
self.age = age
self.salary = salary
 
class childemployee(employee1)://This is a child class
def __init__(self, name, age, salary,id):
self.name = name
self.age = age
self.salary = salary
self.id = id
emp1 = employee1('harshit',22,1000)
 
print(emp1.age)
Output: 22
```

Explanation:

- I am taking the parent class and created a constructor (__init__),  class itself is initializing the attributes with parameters(‘name’, ‘age’ and ‘salary’).

- Created a child class ‘childemployee’ which is inheriting the properties from a parent class and finally instantiated objects ’emp1′ and ’emp2′ against the parameters.

- Finally, I have printed the age of emp1. Well, you can do a hell lot of things like print the whole dictionary or name or salary.

#### Multilevel Inheritance:
Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.

Example:

```python
class employee()://Super class
def __init__(self,name,age,salary):  
self.name = name
self.age = age
self.salary = salary
class childemployee1(employee)://First child class
def __init__(self,name,age,salary):
self.name = name
self.age = age
self.salary = salary
 
class childemployee2(childemployee1)://Second child class
def __init__(self, name, age, salary):
self.name = name
self.age = age
self.salary = salary
emp1 = employee('harshit',22,1000)
emp2 = childemployee1('arjun',23,2000)
 
print(emp1.age)
print(emp2.age)
Output: 22,23
```

Explanation:

It is clearly explained in the code written above, Here I have defined the superclass as employee and child class as childemployee1. Now, childemployee1 acts as a parent for childemployee2.

I have instantiated two objects ’emp1′ and ’emp2′ where I am  passing the parameters “name”, “age”, “salary” for emp1 from superclass  “employee” and “name”, “age, “salary” and “id” from the parent class “childemployee1”

 #### Hierarchical Inheritance:
Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.

Example:


```python
class employee():
def __init__(self, name, age, salary):     //Hierarchical Inheritance
self.name = name
self.age = age
self.salary = salary
 
class childemployee1(employee):
def __init__(self,name,age,salary):
self.name = name
self.age = age
self.salary = salary
 
class childemployee2(employee):
def __init__(self, name, age, salary):
self.name = name
self.age = age
self.salary = salary
emp1 = employee('harshit',22,1000)
emp2 = employee('arjun',23,2000)
 
print(emp1.age)
print(emp2.age)
Output: 22,23

```
Explanation:
In the above example, you can clearly see there are two child class “childemployee1” and “childemployee2”. They are inheriting functionalities from a common parent class that is “employee”.

Objects ’emp1′ and ’emp2′ are instantiated against the parameters ‘name’, ‘age’, ‘salary’.

#### Multiple Inheritance:
Multiple level inheritance enables one derived class to inherit properties from more than one base class.

Example:

```python
class employee1()://Parent class
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class employee2()://Parent class
    def __init__(self,name,age,salary,id):
     self.name = name
     self.age = age
     self.salary = salary
     self.id = id
 
class childemployee(employee1,employee2):
    def __init__(self, name, age, salary,id):
     self.name = name
     self.age = age
     self.salary = salary
     self.id = id
emp1 = employee1('harshit',22,1000)
emp2 = employee2('arjun',23,2000,1234)
 
print(emp1.age)
print(emp2.id)
Output: 22,1234
```

Explanation: In the above example, I have taken two parent class “employee1” and “employee2”.And a child class “childemployee”, which is inheriting both parent class by instantiating the objects ’emp1′ and ’emp2′ against the parameters of parent classes.



