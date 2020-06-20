# Object Oriented programming in Python

[![](https://media.geeksforgeeks.org/wp-content/uploads/OOPs-Concepts.jpg)](http://https://media.geeksforgeeks.org/wp-content/uploads/OOPs-Concepts.jpg)


Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy. 

However, here is small introduction of Object-Oriented Programming (OOP) to bring you at speed −

### Overview of OOP Terminology
- Class − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

- Class variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.

- Data member − A class variable or instance variable that holds data associated with a class and its objects.

- Function overloading − The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.

- Instance variable − A variable that is defined inside a method and belongs only to the current instance of a class.

- Inheritance − The transfer of the characteristics of a class to other classes that are derived from it.

- Instance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

- Instantiation − The creation of an instance of a class.

- Method − A special kind of function that is defined in a class definition.

- Object − A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.

### Creating Classes
The class statement creates a new class definition. The name of the class immediately follows the keyword class followed by a colon as follows −


> class ClassName:
   'Optional class documentation string'
   class_suite   class_suite

The class has a documentation string, which can be accessed via ClassName.__doc__.

The class_suite consists of all the component statements defining class members, data attributes and functions.

Example
Following is the example of a simple Python class −

```python
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
```
The variable empCount is a class variable whose value is shared among all instances of a this class. This can be accessed as Employee.empCount from inside the class or outside the class.

The first method __init__() is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.

You declare other class methods like normal functions with the exception that the first argument to each method is self. Python adds the self argument to the list for you; you do not need to include it when you call the methods.

### Creating Instance Objects
To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.


> "This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)emp2 = Employee("Manni", 5000)

### Accessing Attributes
You access the object's attributes using the dot operator with object. Class variable would be accessed using class name as follows −


> emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
Now, putting all the concepts together Now, putting all the concepts together −

Example:


```python
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
```

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
When the above code is executed, it produces the following result −

Name :  Zara ,Salary:  2000
Name :  Manni ,Salary:  5000
Total Employee 2


# Encapsulation:

An objects variables should not always be directly accessible.

To prevent accidental change, an objects variables can sometimes only be changed with an objects methods. Those type of variables are private variables.

The methods can ensure the correct values are set. If an incorrect value is set, the method can return an error.

Python does not have the private keyword, unlike some other object oriented languages, but encapsulation can be done.

Instead, it relies on the convention: a class variable that should not directly be accessed should be prefixed with an underscore.

```python
class Robot(object):
   def __init__(self):
      self.a = 123
      self._b = 123
      self.__c = 123

obj = Robot()
print(obj.a)
print(obj._b)
print(obj.__c)
```
If you run the program you see:


> 123
123
Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    print(obj.__c)
AttributeError: 'Robot' object has no attribute '__c' AttributeError: 'Robot' object has no attribute '__c' 

Example:

```python
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
```

# Class Variable and Instance Variable(Characteristics of class):

## Introduction
Object-oriented programming allows for variables to be used at the class level or the instance level. Variables are essentially symbols that stand in for a value you’re using in a program.

At the class level, variables are referred to as class variables, whereas variables at the instance level are called instance variables.

When we expect variables are going to be consistent across instances, or when we would like to initialize a variable, we can define that variable at the class level. When we anticipate the variables will change significantly across instances, we can define them at the instance level.

One of the principles of software development is the DRY principle, which stands for don’t repeat yourself. This principle is geared towards limiting repetition within code, and object-oriented programming adheres to the DRY principle as it reduces redundancy.


## Class Variables
Class variables are defined within the class construction. Because they are owned by the class itself, class variables are shared by all instances of the class. They therefore will generally have the same value for every instance unless you are using the class variable to initialize a variable.

Defined outside of all the methods, class variables are, by convention, typically placed right below the class header and before the constructor method and other methods.

A class variable alone looks like this:


>  class Shark:
    animal_type = "fish"

Here, the variable animal_type is assigned the value "fish".


```python
class Shark:
    animal_type = "fish"
new_shark = Shark()
print(new_shark.animal_type)

Output
fish
```
Our program returns the value of the variable.

## Instance Variables
Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different.

Unlike class variables, instance variables are defined within methods.

In the Shark class example below, name and age are instance variables:

> class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age        self.age = age

When we create a Shark object, we will have to define these variables, which are passed as parameters within the constructor method or another method.

> class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

**new_shark = Shark("Sammy", 5)**
As with class variables, we can similarly call to print instance variables:

```python
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark("Sammy", 5)
print(new_shark.name)
print(new_shark.age)

Output
Sammy
5
```
When we run the program above with python shark.py, we’ll receive the following output:

The output we receive is made up of the values of the variables that we initialized for the object instance of new_shark.



# Behaviours of class and its types

- The 3 Types of Methods in Python
There are three types of methods in Python: instance methods, static methods, and class methods.

## Instance Methods in Python
Instance methods are the most common type of methods in Python classes. These are so called because they can access unique data of their instance. If you have two objects each created from a car class, then they each may have different properties. They may have different colors, engine sizes, seats, and so on.

Instance methods must have self as a parameter, but you don’t need to pass this in every time. Self is another Python special term. Inside any instance method, you can use self to access any data or methods that may reside in your class. You won’t be able to access them without going through self.

Finally, as instance methods are the most common, there’s no decorator needed. Any method you create will automatically be created as an instance method, unless you tell Python otherwise.

Example:

```python
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!')
    self.name = 'Decorator_Example'

  def example_function(self):
    """ This method is an instance method! """
    print('I\'m an instance method!')
    print('My name is ' + self.name)
de = DecoratorExample()
de.example_function()
```
The name variable is accessed through self. Notice that when example_function is called, you don’t have to pass self in—Python does this for you.

## Static Methods in Python
Static methods are methods that are related to a class in some way, but don’t need to access any class-specific data. You don’t have to use self, and you don’t even need to instantiate an instance, you can simply call your method:

```python
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!') 

  @staticmethod
  def example_function():
    """ This method is a static method! """
    print('I\'m a static method!')
 
de = DecoratorExample.example_function()
```
The @staticmethod decorator was used to tell Python that this method is a static method.

Static methods are great for utility functions, which perform a task in isolation. They don’t need to (and cannot) access class data. They should be completely self-contained, and only work with data passed in as arguments. You may use a static method to add two numbers together, or print a given string.


## Class Methods in Python
Class methods are the third and final OOP method type to know. Class methods know about their class. They can’t access specific instance data, but they can call other static methods.

Class methods don’t need self as an argument, but they do need a parameter called cls. This stands for class, and like self, gets automatically passed in by Python.

Class methods are created using the @classmethod decorator.

```python
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!') 

  @classmethod
  def example_function(cls):
    """ This method is a class method! """
    print('I\'m a class method!')
    cls.some_other_function()

  @staticmethod
    def some_other_function():
    print('Hello!')
 
de = DecoratorExample()
de.example_function()
```
Class methods are possibly the more confusing method types of the three, but they do have their uses. Class methods can manipulate the class itself, which is useful when you’re working on larger, more complex projects.