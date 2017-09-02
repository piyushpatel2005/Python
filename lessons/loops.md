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

- for loop can also have optional else block which is executed if the for loop terminates prematurely using `break`.

```python
for i in range(1, 10):
  if i == 5:
    break
  print(i)
else:
  print('We found 5 in the data')
```
