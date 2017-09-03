# Functions in Python

A functions is a unit of code that performs a task.Functions are named as a word ending with noun representing what it does.

- You define a function using `def` keyword.

```python
def function_name([arguments]):
  statements
  [return statement]
```

```python
def welcome():
  print("Welcome to the Game")
```

Functions can return a value using `return` keyword.

The main module will have some common line like:

```python
if __name__ == "__main__":
  main()
```

- You can also create module that will have many functions and then that module can be imported.

Module functions can be imported in many ways. For example, suppose `temperature` module has two functions `to_celsius()` and `to_fahrenheit()`. Then,

```python
import temperature
centigrade = temperature.to_celsius(f)
fahrenheit = temperature.to_fahrenheit(c)
```

When you import a module, it will be imported into namespace with the name of the module name. This is the default namespace.

You can import it to specified namespace using `as` keyword.

```python
import temperature as temp
c = temp.to_celsius(f)
```

```python
from temperature import to_celsius

c = to_celsius(f)
# imported only to_celsius() but not to_fahrenheit()
```

```python
from temperature import *
c = to_celsius(f)
```

## Random module

Random module is used to get random numbers.

- random() : returns a random float value that's greater than or equal to 0.0 and less than 1.0
- randint(min, max) : returns random int value that's greater than or equal to min argument and less than or equal to the max argument.
- randrange([start, ] stop [, step]) : returns random vlaue greater than or equal to the start, less than the stop argument and a multiple of the step argument.

```python

import random

number = random.random()
number = random.random() * 100

number = random.randint(1, 100)
number = random.randrange(11, 250, 2)
die = random.randint(1, 6)
```

[Random module game](../examples/random_num.py)


Function can also return multiple comma separated values and the values are assigned in sequence.

If you declare a variable outside all functions, those will become global variables. If you create a new variable inside the function with the same name, that variable will become local variable and will shadow global variable.

You can read values of global variable inside a function, but you cannot change that variable directly. If you want to modify the variable, you need to use `global <variable_name>`.

```python
tax = 0.0

def calc_tax(amount, tax_rate):
  global tax      # access global variable
  tax = amount * tax_rate   # change global variable
```
