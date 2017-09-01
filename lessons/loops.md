# Loops

Loops can help reduce the repetitive code.

```python
while condition:
  .... statements ....
  ... ... ...
```

[While loop example](examples/while.py)

In a loop, `break` or `continue` can be used to break the loop prematurely or to skip one of the iterations based on a condition.

**For** loop:

```python
for i in range(0, 5):
  print(i)
```

Function can also return multiple comma separated values and the values are assigned in sequence.

If you declare a variable outside all functions, those will become global variables. If you create a new variable inside the function with the same name, that variable will become local variable and will shadow global variable.

You can read values of global variable inside a function, but you cannot change that variable directly. If you want to modify the variable, you need to use `global <variable_name>`.

```python
tax = 0.0

def calc_tax(amount, tax_rate):
  global tax      # access global variable
  tax = amount * tax_rate   # change global variable
```
