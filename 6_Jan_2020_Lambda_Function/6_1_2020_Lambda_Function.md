**Functional programming is all about
expressions. We may say that the Functional
programming is an expression oriented
programming**.

- Expression oriented functions of Python provides
are:

1. lambda

2. map(aFunction, aSequence)

3. filter(aFunction, aSequence)

4. reduce(aFunction, aSequence)

5. list comprehension

## lambda function

- A way to create small anonymous functions, i.e.
functions without a name.
- Mainly used in combination with the functions
filter(), map() and reduce().

Syntax:
lambda argument_list: expression

Example:

```python
def add(x,y):
return x+y
# call the function
add(2,3) # output : 5
#Functional approach
add = lambda x, y : x + y
print(add(2,3))

Output:
5
```

Example:

```python
f = lambda x: x<100
print(f(90))

Output:
True
```

## Map() function

The map(aFunction, aSequence) function applies
a passed-in function to each item in an iterable
object and returns a list containing all the function
call results.

Ex:

```python
items = [1, 2, 3, 4, 5]
def sqr(x):
return x ** 2
print(list(map(sqr, items)))

Output:
[1, 4, 9, 16, 25]
```

Example:

##### python 3

```python
items = [1, 2, 3, 4, 5]
print(list(map((lambda x: x **2), items)))
```

While we still use lamda as a aFunction, we can have a list
of functions as aSequence.

Ex:

```python
def square(x):
return (x**2)
def cube(x):
return (x**3)
funcs = [square, cube]
for r in range(5):
value = list(map(lambda x: x(r), funcs))
print(value)

Output:
[0, 0]
[1, 1]
[4, 8]
[9, 27]
[16, 64]
```

Because using map is equivalent to for loops, with an extra code
we can always write a general mapping utility.

Example: 

#### using map() function

```python
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))

Output:
[11,22,33]
```

## filter() function

The **filter(aFunction, aSequence)** function
applies a passed-in function to each item in an
iterable object and extracts each element in the
sequence for which the function returns True.

Example:-

```python
list(range(-5,5))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print(list(filter((lambda x: x < 0), range(-5,5))))
print(list(map((lambda x: x < 0), range(-5,5))))

Output:-
[-5, -4, -3, -2, -1]
[True, True, True, True, True, False, False, False,
False, False]
```

Example:

```python
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(filter(lambda x: x in a, b))

Output:-
[2, 3, 5, 7]
```

## reduce() function

**reduce(aFunction, aSequence)**

It applies a rolling computation to sequential pairs of values
in a list.

Example:

```python
from functools import reduce #python3
print(reduce( (lambda x, y: x * y), [1, 2, 3, 4] ))

Output:
24


#Determining the maximum of a list of numerical
values by using reduce:
from functools import reduce
f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))

Output:
102

#Calculating the sum of the numbers from 1 to 100:
from functools import reduce
print(reduce(lambda x, y: x+y, range(1,101)))

Output:
5050
```