# Functions in Python:
- A block of organized, reusable code that is used to perform a
single, related action.
- Provides better modularity for your application and a high
degree of code reusing.
- Python gives you many built-in functions like print(), etc. but you
can also create your own functions. These functions are
called user-defined functions.

[![](https://miro.medium.com/max/1024/1*c9rggC6SzDXIUnoR9JMAKA.png)](http://https://miro.medium.com/max/1024/1*c9rggC6SzDXIUnoR9JMAKA.png)

[![](https://www.brainkart.com/media/extra3/cgRNUFy.jpg)](http://https://www.brainkart.com/media/extra3/cgRNUFy.jpg)

#### Defining a Function

------------



- You can define functions to provide the required functionality. Here are
simple rules to define a function in Python.
- Function blocks begin with the keyword def followed by the function name and
parentheses ( ( ) ).
- Any input parameters or arguments should be placed within these parentheses.
You can also define parameters inside these parentheses.
- The first statement of a function can be an optional statement - the
documentation string of the function or docstring.
- The code block within every function starts with a colon (:) and is indented.
- The statement return [expression] exits a function, optionally passing back an
expression to the caller. A return statement with no arguments is the same as
return None.

Syntax & Example

```python
 def functionname( parameters ):

"function_docstring“
function_suite
return [expression]

 def printme( str ):

"This prints a passed string into this function“
print (str)
return
```

#### Calling a Function

------------



- Defining a function gives it a name, specifies the parameters
that are to be included in the function and structures the blocks
of code.

- Once the basic structure of a function is finalized, you can
execute it by calling it from another function or directly from the
Python prompt.


```python
 # Function definition is here
 def printme( str ):

"This prints a passed string into this function“
print (str)
return

# Now you can call printme function
 printme("This is first call to the user defined function!")
 printme("Again second call to the same function")
 
 Output:-
This is first call to the user defined function!
Again second call to the same function
```


#### Pass by Reference vs Value

------------



- All parameters (arguments) in the Python language are passed
by reference.
- Means if you change what a parameter refers to within a
function, the change also reflects back in the calling function.

 Example 1:-
 
```python
def changeme( mylist ):

"This changes a passed list into this function"
print ("Values inside the function before change: ", mylist)
mylist[2]=50
print ("Values inside the function after change: ", mylist)
return

 mylist = [10,20,30]
 changeme( mylist )
 print ("Values outside the function: ", mylist)

Output:-
Values inside the function before change: [10, 20, 30]
Values inside the function after change: [10, 20, 50]
Values outside the function: [10, 20, 50]
```
Example 2:-
```python
def changeme( mylist ):

"This changes a passed list into this function"
mylist = [1,2,3,4] # This would assi new reference in mylist
print ("Values inside the function: ", mylist)
return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

Output:-
Values inside the function: [1, 2, 3, 4]
Values outside the function: [10, 20, 30]
```

#### Function Arguments

------------



 You can call a function by using the following types of formal
arguments −
 - Required arguments
 - Keyword arguments
 - Default arguments
 - Variable-length arguments

#### Required Arguments/ Positional Arguments

- Required arguments are the arguments passed to a function in
correct positional order.
- Here, the number of arguments in the function call should match
exactly with the function definition.

Example:-

```python
 def printme( str ):
"This prints a passed string into this function"
print (str)
return
printme()

Output:-
Traceback (most recent call last):
File "test.py", line 11, in <module>
printme();
TypeError: printme() takes exactly 1 argument (0 given)
```


#### Keyword Arguments

------------



- Keyword arguments are related to the function calls.
- When you use keyword arguments in a function call, the caller
identifies the arguments by the parameter name.
- This allows you to skip arguments or place them out of order
because the Python interpreter is able to use the keywords
provided to match the values with parameters.

Example:-

```python
def printme( str ):
"This prints a passed string into this function"
print (str)
return
printme( str = "My string")

Output:-
My string
```
#### Default Arguments

------------



- A default argument is an argument that assumes a default value if a value
is not provided in the function call for that argument.
Example:-

```python
def printinfo( name, age = 35 ):
"This prints a passed info into this function"
print ("Name: ", name)
print ("Age ", age)
return
printinfo( age = 50, name = "miki" )
printinfo( name = "miki" )

Output:-
Name: miki
Age 50
Name: miki
Age 35
```
# User Defined Functions:

[![](https://static.thegeekstuff.com/wp-content/uploads/2019/05/python-functions.png)](http://https://static.thegeekstuff.com/wp-content/uploads/2019/05/python-functions.png)

**Python - User-Defined Functions**
Python includes many built-in functions. These functions perform a predefined task and can be called upon in any program, as per requirement. However, if you don't find a suitable built-in function to serve your purpose, you can define one. We will now see how to define and use a function in a Python program.

**Defining a Function**
A function is a reusable block of programming statements designed to perform a certain task. To define a function, Python provides the def keyword. The following is the syntax of defining a function.

**Syntax:**

```python
def function_name(parameters):
    "function docstring"
    statement1
    statement2
    ...
    ...
    return [expr]
```
The keyword def is followed by a suitable identifier as the name of the function and parentheses. One or more parameters may be optionally mentioned inside parentheses. The **:** symbol after parentheses starts an indented block.

The first statement in this block is an explanatory string which tells something about the functionality. It is called a docstring and it is optional. It is somewhat similar to a comment. Subsequent statements that perform a certain task form the body of the function.

The last statement in the function block includes the return keyword. It sends an execution control back to calling the environment. If an expression is added in front of return, its value is also returned.

Example: 

```python
def SayHello():
    ""First line is docstring. When called, a greeting message will be displayed""
    print ("Hello! Welcome to Python ")
    return
#To call a defined function, just use its name as a statement anywhere in the code. For example, the above function can be called as SayHello() and it will show the following output.

SayHello()
Hello! Welcome to Python
```

# Built-In Functions:
[![](https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/01/Python-Built-in-functions-1024x536-1.jpg)](http://https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/01/Python-Built-in-functions-1024x536-1.jpg)

**Python Built-in Functions**
The Python built-in functions are defined as the functions whose functionality is pre-defined in Python. The python interpreter has several functions that are always present for use. These functions are known as Built-in Functions.
To list some are:
1. abs()
2. all()
3. bin()
4. bool()
5. bytes()
6. callable()
7. compile()
8. execute()

**Python all() Function**
The python all() function accepts an iterable object (such as list, dictionary, etc.). It returns true if all items in passed iterable are true. Otherwise, it returns False. If the iterable object is empty, the all() function returns True.

Example

```python
# all values true  
k = [1, 3, 4, 6]  
print(all(k))  
  
# all values false  
k = [0, False]  
print(all(k))  
  
# one false value  
k = [1, 3, 7, 0]  
print(all(k))  
  
# one true value  
k = [0, False, 5]  
print(all(k))  
  
# empty iterable  
k = []  
print(all(k))  

Output:
True
False
False
False
True
```
**Python bin() Function**
The python bin() function is used to return the binary representation of a specified integer. A result always starts with the prefix 0b.

Example

```python
x =  10  
y =  bin(x)  
print (y)  

Output:
0b1010
```
**Python bool()**
The python bool() converts a value to boolean(True or False) using the standard truth testing procedure.

Example

```python
test1 = []  
print(test1,'is',bool(test1))  
test1 = [0]  
print(test1,'is',bool(test1))  
test1 = 0.0  
print(test1,'is',bool(test1))  
test1 = None  
print(test1,'is',bool(test1))  
test1 = True  
print(test1,'is',bool(test1))  
test1 = 'Easy string'  
print(test1,'is',bool(test1))  
Output:

[] is False
[0] is True
0.0 is False
None is False
True is True
Easy string is True
```
# Recursive Functions:
[![](https://www.cdn.geeksforgeeks.org/wp-content/uploads/Recursive-Functions-in-c.png)](http://https://www.cdn.geeksforgeeks.org/wp-content/uploads/Recursive-Functions-in-c.png)


**Introduction**
When we think about repeating a task, we usually think about the for and while loops. These constructs allow us to perform iteration over a list, collection, etc.

However, there's another form of repeating a task, in a slightly different manner. By calling a function within itself, to solve a smaller instance of the same problem, we're performing recursion.

These functions call themselves until the problem is solved, practically dividing the initial problem to a lot of smaller instances of itself – like for an example, taking small bites of a larger piece of food.

The end goal is to eat the entire plate of hot pockets, you do this by taking a bite over and over. Each bite is a recursive action, after which you undertake the same action the next time. You do this for every bite, evaluating that you should take another one to reach the goal, until there are no hot pockets left on your plate.

**What is Recursion?**
As stated in the introduction, recursion involves a process calling itself in the definition. A recursive function generally has two components:

The base case which is a condition that determines when the recursive function should stop
The call to itself


```python
#Assume that remaining is a positive integer
def hi_recursive(remaining):
    #The base case
    if remaining == 0:
        return
    print('hi')

    # Call to function, with a reduced remaining count
    hi_recursive(remaining - 1)
```
The base case for us is if the remaining variable is equal to 0 i.e. how many remaining "hi" strings we must print. The function simply returns.

After the print statement, we call hi_recursive again but with a reduced remaining value. This is important! If we do not decrease the value of remaining the function will run indefinitely. Generally, when a recursive function calls itself the parameters are changed to be closer to the base case.

Let's visualize how it works when we call hi_recursive(3):

[![](https://s3.amazonaws.com/stackabuse/media/understanding-recursion-with-python-1.jpg)](http://https://s3.amazonaws.com/stackabuse/media/understanding-recursion-with-python-1.jpg)

After the function prints 'hi', it calls itself with a lower value for remaining until it reaches 0. At zero, the function returns to where it was called in hi_recursive(1), which returns to where it was called in hi_recursive(2) and that ultimately returns to where it was called in hi_recursive(3).

#### Factorial Numbers Factorial Numbers
You may recall that a factorial of a positive integer, is the product of all integers preceding it. The following example would make it clearer:

**5! = 5 x 4 x 3 x 2 x 1 = 120**
The exclamation mark denotes a factorial, and we see that we multiply 5 by the product of all the integers from 4 till 1. What if someone enters 0? It's widely understood and proven that 0! = 1. Now let's create a function like below:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```
We cater for the cases where 1 or 0 is entered, and otherwise we multiply the current number by the factorial of the number decreased by 1.

A simple verification in your Python interpreter would show that factorial(5) gives you 120.

It is possible to return multiple values from a function in the form of tuple, list, dictionary or an object of a user defined class

# Return Multipe Values
**Return as Tuple**
```python
def function():
      a=10; b=10
      return a,b

x=function()
type(x)
<class 'tuple'>
x
(10, 10)
x,y=function()
x,y
(10, 10)
```
**Return as list**

```python
def function():
      a=10; b=10
      return [a,b]

x=function()
x
[10, 10]
type(x)
<class 'list'>
```
**Return as dictionary**

```python
def function():
      d=dict()
      a=10; b=10
      d['a']=a; d['b']=b
      return d

x=function()
x
{'a': 10, 'b': 10}
type(x)
<class 'dict'>
```

**Return as object of user defined class**

```python
class tmp:
def __init__(self, a,b):
self.a=a
self.b=b

def function():
      a=10; b=10
      t=tmp(a,b)
      return t

x=function()
type(x)
<class '__main__.tmp'>
x.a
10
x.b
10
```
# What is a Nested Function?
Functions are one of the "first-class citizens" of Python, which means that functions are at the same level as other Python objects like integers, strings, modules, etc. They can be created and destroyed dynamically, passed to other functions, returned as values, etc.

Python supports the concept of a "nested function" or "inner function", which is simply a function defined inside another function. In the rest of the article, we will use the word "inner function" and "nested function" interchangeably.

There are various reasons as to why one would like to create a function inside another function. The inner function is able to access the variables within the enclosing scope. In this article, we will be exploring various aspects of inner functions in Python.

### Defining an Inner FunctionDefining an Inner Function
To define an inner function in Python, we simply create a function inside another function using the Python's def keyword. Here is an example:

def function1(): 

```python
# outer function
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()

function1()

Output
Hello from outer function
Hello from inner function
```
In the above example, function2() has been defined inside function1(), making it an inner function. To call function2(), we must first call function1(). The function1() will then go ahead and call function2() as it has been defined inside it.

It is important to mention that the outer function has to be called in order for the inner function to execute. If the outer function is not called, the inner function will never execute. 

### Why use Inner Functions?
**Encapsulation**
A function can be created as an inner function in order to protect it from everything that is happening outside of the function. In that case, the function will be hidden from the global scope. Here is an example:

def outer_function(x):
   ```python
 # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

inner_increment(5)
#outer_function(5)

Output
Enter your email...
Traceback (most recent call last):
  File "C:/Users/admin/inner.py", line 7, in <module>
    inner_increment(5)
NameError: name 'inner_increment' is not defined
```
In the above code, we are trying to call the inner_increment() function, but instead we got an error.

Now, comment out the call to inner_increment() and uncomment the call to outer_function() as shown below:

```python
def outer_function(x):
    # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

#inner_increment(5)
outer_function(5)

Output
5 7
```

The script above shows that the inner function, that is, inner_increment() is protected from what is happening outside it since the variable x inside the inner_increment function is not affected by the value passed to the parameter x of the outer function. In other words, the variables inside the inner function is not accessible outside it. There is a great advantage with such a design pattern. After checking all arguments in the outer function, we can safely skip error checking within the inner function.