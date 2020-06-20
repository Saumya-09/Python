# Function Arguments

------------



 You can call a function by using the following types of formal
arguments −
 - Required arguments/Positional arguments
 - Keyword arguments
 - Default arguments
 - Variable-length arguments

#### Required Arguments/ Positional Arguments

--------

- Required arguments are the arguments passed to a function in
correct positional order.
- Here, the number of arguments in the function call should match
exactly with the function definition.

Example:-

```python
 def printme( str ):
"This prints a passed string into this function"
    print (str)
return printme()

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
return printme( str = "My string")

Output:-
My string
```

```python
def divide(a,b):
	return a/b
divide(3,2)
divide(a=1,b=2)
divide(b=2,a=1)

Output:
0.5
0.5
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

#### Variable-length arguments
- You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is this −

> def functionname([formal_args,] *var_args_tuple ):
>	"function_docstring"
>	function_suite
>	return [expression]

An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call. Following is a simple example −

Example:

```python
def printinfo( arg1, *vartuple ):
	print arg1
	for var in vartuple:
		print var
		return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

Output is:
10
Output is:
70
60
50
```


#### The Anonymous Functions
- These functions are called anonymous because they are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions.

- Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.

- An anonymous function cannot be a direct call to print because lambda requires an expression

- Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.

Syntax
The syntax of lambda functions contains only a single statement, which is as follows −

> lambda [arg1 [,arg2,.....argn]]:expression

Example:

```python
sum = lambda arg1, arg2: arg1 + arg2;
# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )
When the above code is executed, it produces the following result −

Value of total :  30
Value of total :  40
```