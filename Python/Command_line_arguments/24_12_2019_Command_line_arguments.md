## What is Console ?



Console (also called Shell) is basically a command line interpreter that takes input from the user i.e one command at a time and interprets it. If it is error free then it runs the command and gives required output otherwise shows the error message. A Python Console looks like this.

[![Console](https://www.tutorialsteacher.com/Content/images/python/python-shell.png "Console")](http://https://www.tutorialsteacher.com/Content/images/python/python-shell.png "Console")


Here we write command and to execute the command just press enter key and your command will be interpreted.

# Command Line Arguments:
Till now, we have taken input in python using raw_input() or input() [for integers]. There is another method that uses command line arguments. The command line arguments must be given whenever we want to give the input before the start of the script, while on the other hand, raw_input() is used to get the input while the python program / script is running.

The command line arguments in python can be processed by using either ‘sys’ module or ‘argparse’ module.


### Example
> import sys 
 argumentList = sys.argv 
 print sys.argv[0]  
> print sys.argv[1] 

>### Output
> ['program1.py', 'test', '1']
>
> program1.py
>
> test

```python
import argparse

parser=argparse.ArgumentParser(description= 'Perimetetr of a rectangle')
parser.add_argument('-l','--length', type = int , required= True , help= 'Length of Rectangle')
parser.add_argument('-b','--breadth',type = int , required= True , hrlp= 'Breadth of Rectangle')
args=parser.parse_args()


if __name__=='__main__':
	print(Perimeter(args.length, args.breadth))
```

### Variable Arguments

args (star) and kwargs(double star)
Both ‘args’ and ‘kwargs’ are used to get arbitrary number of arguments in a function.
args will give us all the function parameters in the form of a list and kwargs will give us all the keyword arguments except for those corresponding to formal parameter as dictionary.


# Input in Python
To receive information through the keyboard, Python uses either the input() or raw_input() functions (more about the difference between the two in the following section). These functions have an optional parameter, commonly known as prompt, which is a string that will be printed on the screen whenever the function is called.

When one of the input() or raw_input() functions is called, the program flow stops until the user enters the input via the command line. To actually enter the data, the user needs to press the ENTER key after inputing their string.  The entered string will simply be submitted to the application.

#### Comparing the input and raw_input Functions

 ------------
The difference when using these functions only depends on what version of Python is being used. For Python 2, the function raw_input() is used to get string input from the user via the command line, while the input() function returns will actually evaluate the input string and try to run it as Python code.

In Python 3, raw_input() function has been deprecated and replaced by the input() function and is used to obtain a user's string through the keyboard. And the input() function of Python 2 is discontinued in version 3. To obtain the same functionality that was provided by Python 2's input() function, the statement eval(input()) must be used in Python 3.

#### Example
> txt = raw_input("Type something to test this out: ")
>
> print "Is this what you just said?", txt

>#### Output
> Type something to test this out: Let the Code be with you!
    Is this what you just said? Let the Code be with you!



#### String and Numeric input

------------
The input() function, by default, will convert all the information it receives into a string. The previous example we showed demonstrates this behavior.

Numbers, on the other hand, need to be explicitly handled as such since they come in as strings originally. The following example demonstrates how numeric type information is received:

#### Example

 > test_text = input ("Enter a number: ")
 >
 > test_number = int(test_text)
 >
 > print ("The number you entered is: ", test_number)

>#### Output
>Enter a number: 13
The number you entered is: 13


# Output in Python

------------



In addition to obtaining data from the user, a program will also usually need to present data back to the user. You can display program data to the console in Python with print().

Simple print() function can be used to print output in the python.
There is alot of string formatting and other things that can be done in python, but if we want to display anything than print() can be used.

# Variables in Python
Variables are used to store information to be referenced and manipulated in a computer language . They also provide a way of labelling data with a detailed naming, so our programs can be understood more clearly by the reader and ourselves.

### Python Variables

------------


Every variable in Python is considered as an object. Variables in Python follow the standard nomenclature of an alphanumeric name beginning in a letter or underscore. Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. You do not need to declare variables before using them, or declare their type. Variable names are case sensitive . Most variables in Python are local in scope to their own function or class. Global variables , however, can be declared with the global keyword.

### Assigning Values to Variables

------------


When you assign a variable, you use the = symbol. The name of the variable goes on the left and the value you want to store in the variable goes on the right.
#### Examples
> a=10
>
> firstname= "Saumya"
>
> mile= 1000.0

### Multiple Assignment

------------



Python allows you to assign a single value to several variables simultaneously.  Example:-

> a = b = c = 1


You can also assign multiple objects to multiple variables. Example:-

> a, b, c = 1, 2.0, "john"


####  Rules for declaring variables
------------

Variables are the example of identifiers. An Identifier is used to identify the literals used in the program. The rules to name an identifier are given below.

- The first character of the variable must be an alphabet or underscore ( _ ).
- All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore or digit (0-9).
- Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
- Identifier name must not be similar to any keyword defined in the language.
- Identifier names are case sensitive for example my name, and MyName is not the same.
- Examples of valid identifiers : a123, _n, n_9, etc.
- Examples of invalid identifiers: 1a, n%4, n 9, etc.

#### Referencing variables:

```python
 m = 300
 n = 300
 id(m)
60062304
id(n)
60062896
```
With the statement m = 300, Python creates an integer object with the value 300 and sets m as a reference to it. n is then similarly assigned to an integer object with value 300—but not the same object. Thus, they have different identities, which you can verify from the values returned by id().

```python
 m = 30
 n = 30
 id(m)
1405569120
 id(n)
1405569120
```
Here, m and n are separately assigned to integer objects having value 30. But in this case, id(m) and id(n) are identical!

For purposes of optimization, the interpreter creates objects for the integers in the range **[-5, 256]** at startup, and then reuses them during program execution. Thus, when you assign separate variables to an integer value in this range, they will actually reference the same object.

# Operators in Python

Python Operator falls into 7 categories:

- Python Arithmetic Operator
- Python Relational Operator
- Python Assignment Operator
- Python Logical Operator
- Python Membership Operator
- Python Identity Operator
- Python Bitwise Operator

### Python Arithmetic Operator
These Python arithmetic operators include Python operators for basic mathematical operations.

 -  Addition(+)

Adds the values on either side of the operator.

> 3+4
Output: 7

- Subtraction(-)

Subtracts the value on the right from the one on the left.

> 3-4
Output: -1

- Multiplication(*)

Multiplies the values on either side of the operator.

> 3*4
Output: 12

- Division(/)

Divides the value on the left by the one on the right. Notice that division results in a floating-point value.

> 3/4
Output: 0.75

- Exponentiation(**)

Raises the first number to the power of the second.

> 3**4
Output: 81

- Floor Division(//)

Divides and returns the integer value of the quotient. It dumps the digits after the decimal.

> 3//4
> 4//3
Output: 1

> 10//3
Output: 3

- Modulus(%)

Divides and returns the value of the remainder.

> 3%4
Output: 3

> 4%3
Output: 1

> 10.5%3
Output: 1.5

### Python Relational Operator 

Relational Python Operator carries out the comparison between operands. They tell us whether an operand is greater than the other, lesser, equal, or a combination of those.

- Less than(<)

This operator checks if the value on the left of the operator is lesser than the one on the right.

> 3<4
Output: True

- Greater than(>)

It checks if the value on the left of the operator is greater than the one on the right.

> 3>4
Output: False

- Less than or equal to(<=)

It checks if the value on the left of the operator is lesser than or equal to the one on the right.

> 7<=7
Output: True

- Greater than or equal to(>=)

It checks if the value on the left of the operator is greater than or equal to the one on the right.

> 0>=0
Output: True

- Equal to(= =)

This operator checks if the value on the left of the operator is equal to the one on the right. 1 is equal to the Boolean value True, but 2 isn’t. Also, 0 is equal to False.

> 3==3.0
Output: True

> 1==True
Output: True

> 7==True
Output: False

> 0==False
Output: True

> 0.5==True
Output: False

- Not equal to(!=)

It checks if the value on the left of the operator is not equal to the one on the right. The Python operator <> does the same job, but has been abandoned in Python 3.

When the condition for a relative operator is fulfilled, it returns True. Otherwise, it returns False. You can use this return value in a further statement or expression.

> 1!=1.0
Output: False
> -1<>-1.0
This causes a syntax error

### Python Assignment operator

An assignment operator assigns a value to a variable. It may manipulate the value by a factor before assigning it. We have 8 assignment operators- one plain, and seven for the 7 arithmetic python operators.

- Assign(=)

Assigns a value to the expression on the left. Notice that = = is used for comparing, but = is used for assigning.

> a=7
> print(a)
Output: 7

- Add and Assign(+=)

Adds the values on either side and assigns it to the expression on the left. a+=10 is the same as a=a+10.

The same goes for all the next assignment operators.

> a+=2
> print(a)
Output: 9

- Subtract and Assign(-=)

Subtracts the value on the right from the value on the left. Then it assigns it to the expression on the left.
> a-=2
> print(a)
Output: 7

- Divide and Assign(/=)

Divides the value on the left by the one on the right. Then it assigns it to the expression on the left.

> a/=7
> print(a)
Output: 1.0

- Multiply and Assign(*=)

Multiplies the values on either sides. Then it assigns it to the expression on the left.

> a*=8
> print(a)
Output: 8.0

- Modulus and Assign(%=)

Performs modulus on the values on either side. Then it assigns it to the expression on the left.

> a%=3
> print(a)
Output: 2.0

- Exponent and Assign(**=)

Performs exponentiation on the values on either side. Then assigns it to the expression on the left.

> a**=5
> print(a)
Output: 32.0

- Floor-Divide and Assign(//=)

Performs floor-division on the values on either side. Then assigns it to the expression on the left.

> a//=3
> print(a)
Output: 10.0


### Python Logical Operator
These are conjunctions that you can use to combine more than one condition. We have three Python logical operator – and, or, and not that come under python operators.

- and

If the conditions on both the sides of the operator are true, then the expression as a whole is true.

> a=7>7 and 2>-1
> print(a)
Output: False

- or

The expression is false only if both the statements around the operator are false. Otherwise, it is true.

> a=7>7 or 2>-1
> print(a)
Output: True

> 7 and 0 or 5
Output: 5

##### ‘and’ returns the first False value or the last value; ‘or’ returns the first True value or the last value

- not

This inverts the Boolean value of an expression. It converts True to False, and False to True. As you can see below, the Boolean value for 0 is False. So, not inverts it to True.

> a=not(0)
> print(a)
Output: True

### Membership Python Operator
These operators test whether a value is a member of a sequence. The sequence may be a list, a string, or a tuple. We have two membership python operators- ‘in’ and ‘not in’.

- in

This checks if a value is a member of a sequence. In our example, we see that the string ‘fox’ does not belong to the list pets. But the string ‘cat’ belongs to it, so it returns True. Also, the string ‘me’ is a substring to the string ‘disappointment’. Therefore, it returns true.

> pets=[‘dog’,’cat’,’ferret’]
> ‘fox’ in pets
Output: False

>‘cat’ in pets
Output: True

> ‘me’ in ‘disappointment’
Output: True

- not in

Unlike ‘in’, ‘not in’ checks if a value is not a member of a sequence.

> ‘pot’ not in ‘disappointment’
Output: True

### Python Identity Operator
These operators test if the two operands share an identity. We have two identity operators- ‘is’ and ‘is not’.

- is

If two operands have the same identity, it returns True. Otherwise, it returns False. Here, 2 is not the same as 20, so it returns False. Also, ‘2’ and “2” are the same. The difference in quotes does not make them different. So, it returns True.

> 2 is 20
Output: False

> ‘2’ is “2”
Output: True

- is not

2 is a number, and ‘2’ is a string. So, it returns a True to that.

> 2 is not ‘2’
Output: True

### Python Bitwise Operator

- Binary AND(&)

It performs bit by bit AND operation on the two values. Here, binary for 2 is 10, and that for 3 is 11. &-ing them results in 10, which is binary for 2. Similarly, &-ing 011(3) and 100(4) results in 000(0).

> 2&3
Output: 2
> 3&4
Output: 0

- Binary OR(|)

It performs bit by bit OR on the two values. Here, OR-ing 10(2) and 11(3) results in 11(3).

> 2|3
Output: 3

- Binary XOR(^)

It performs bit by bit XOR(exclusive-OR) on the two values. Here, XOR-ing 10(2) and 11(3) results in 01(1).

> 2^3
Output: 1

- Binary Ones Complement(~)

It returns the one’s complement of a number’s binary. It flips the bits. Binary for 2 is 00000010. Its one’s complement is 11111101. This is binary for -3. So, this results in -3. Similarly, ~1 results in -2.

>~-3
Output: 2

Again, ones complement of -3 is 2.

- Binary Left-Shift(<<)

It shifts the value of the left operand the number of places to the left that the right operand specifies. Here, binary of 2 is 10. 2<<2 shifts it two places to the left. This results in 1000, which is binary for 8.

> 2<<2
Output: 8

- Binary Right-Shift(>>)

It shifts the value of the left operand the number of places to the right that the right operand specifies. Here, binary of 3 is 11. 3>>2 shifts it two places to the right. This results in 00, which is binary for 0. Similarly, 3>>1 shifts it one place to the right. This results in 01, which is binary for 1.

> 3>>2
> 3>>1
Output: 1

### Precedence in Python
Python has well-defined rules for specifying the order in which the operators in an expression are evaluated when the expression has several operators. For example, multiplication and division have a higher precedence than addition and subtraction. Precedence rules can be overridden by explicit parentheses.


- Precedence Order
When two operators share an operand, the operator with the higher precedence goes first. For example, since multiplication has a higher precedence than addition, 
a + b * c is treated as a + (b * c), and a * b + c is treated as (a * b) + c.


- Associativity
When two operators share an operand and the operators have the same precedence, then the expression is evaluated according to the associativity of the operators. For example, since the **operator has right-to-left associativity, a ** b ** c is treated as a ** (b ** c). On the other hand, since the / operator has left-to-right associativity, a / b / c is treated as (a / b) / c.


- Precedence and Associativity of Python Operators
The Python documentation on operator precedence contains a table that shows all Python operators from lowest to highest precedence, and notes their associativity. Most programmers do not memorize them all, and those that do still use parentheses for clarity.


- Order of Evaluation
In Python, the left operand is always evaluated before the right operand. That also applies to function arguments.

Python uses short circuiting when evaluating expressions involving the and or or operators. When using those operators, Python does not evaluate the second operand unless it is necessary to resolve the result. That allows statements such as if (s != None) and (len(s) < 10): 

# Numbers in Python

Number data types store numeric values. They are immutable data types, means that changing the value of a number data type results in a newly allocated object.

Number objects are created when you assign a value to them. For example −

>var1 = 1
>var2 = 10

You can also delete the reference to a number object by using the del statement. The syntax of the del statement is −
>del var1[,var2[,var3[....,varN]]]]

You can delete a single object or multiple objects by using the del statement. For example −
>del var
>del var_a, var_b

Python supports four different numerical types −

1. int (signed integers) − They are often called just integers or ints, are positive or negative whole numbers with no decimal point.

2. long (long integers ) − Also called longs, they are integers of unlimited size, written like integers and followed by an uppercase or lowercase L.

3. float (floating point real values) − Also called floats, they represent real numbers and are written with a decimal point dividing the integer and fractional parts. Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).

4. complex (complex numbers) − are of the form a + bJ, where a and b are floats and J (or j) represents the square root of -1 (which is an imaginary number). The real part of the number is a, and the imaginary part is b. Complex numbers are not used much in Python programming.
