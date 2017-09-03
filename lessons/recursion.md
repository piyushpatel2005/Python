# Recursion

Recursion occurs when a function calls itself.

```python
def display_message():
  print("Press Ctrl+C to stop!")
  display_message()
```

Each recursive function calls itself. Recursive function stops only when the *base case* is reached.

```python
def add_numbers(upper):
  total = 0
  for number in range(upper + 1):
    total += number
  return number
```

```python
def add_numbers(upper):
  if upper == 0:
    return upper
  else:
    return upper + add_numbers(upper - 1)

def main():
  total = add_numbers(5)  # total = 15
```

The number of recursive function calls that are on the stack at the same time can be referred to as *recursion depth*.

[Factorial example](../examples/factorial.py)

```python
# Fibonacci series
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  n1 = 0
  n2 = 1
  fib = 0
  for i in range(2, n+1):
    fib = n1 + n2
    n1 = n2
    n2 = fib
  return fib
```
