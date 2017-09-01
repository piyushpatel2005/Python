# Python

- developed by Guido Van Rossum in 1990s.
- open source
- Python 3 developed in 2008
- syntax easier to read and use than most other languages
- supports development of wide range of programs, games, web applications, system administration.
- Python files are created with .py extension
- platform-independent
- You can enter Python interactive shell using simple command on Terminal. Type `python` and it will start interactive shell with `>>>`.
- In Python, shebang (#!) line is used to indicate which interpreter is used for a particular program.

```python
#! /usr/bin/env python3

counter = 0
score_total = 0
test_score = 0

while test_score != 999:
  test_score = int(input("Enter test score: "))
  if test_score >= 0 and test_score <= 100:
    score_total += test_score
    counter += 1
average_score = round(score_total / counter)

print("Total score: " + str(score_total))
print("Average score: " + str(average_score))
```

- Python uses indentation to create blocks of statements in loops and conditionals. So, when you need to write long code in two sentences, you need to be cautious. Here, are two ways to do it. They can be put to separate line using (\) and (+).

```python
print ("Total score: " + str(total)
    + "\nAverage Score: " + str(average))
print("Total score : " + str(total) \
      + "\nAverage : " + str(average))
```

- In Python, comments are created using pound sign (#)
- To run a Python script, you can use `python <scriptname>` command.
- In Python comments are written with pound (#) symbol.
- In Python community, mostly underscores are used in naming a variable.

Python supports following arithmetic operations.

* : Multiplication
+ : Addition
- : Subtraction
/ : Division
// : Integer Division
** : exponential
% : Modulo

Python also like every other language uses (\) for special characters. (\r, \n, \t, etc.)

- int(data) : converts data argument to int type and returns that int value.
- float(data) : converts data argument to float type and returns that value.
- round(number [, digits]) - rounds the number argument to number of decimal digits in the digits argument. If no digit specified then rounds to nearest integer.
- strdata.lower() - converts uppercase letters to lowercase
- strdata.upper() - converts lowercase to uppercase
- range(start, stop[, step]) - returns integer values from the start to the stop but not including stop (with steps of the value step).

```python
# Interate five times
for i in range(5):
  print(i, end=" ")   # 0 1 2 3 4
```

You can get help for a function using `help(function name)` in Python.

- When you write your own module, you can use """ to create doc strings which will be displayed when you use help() function.

We can assign multiple values like this:

```python
x, y, z = 1, 2, 3
```




**Table of Contents:**

1. [Taking inputs and printing output](lessons/io.md)
2. [Conditionals](lessons/conditionals.md)
3. [Loops](lessons/loops.md)
4. [Functions](lessons/functions.md)
5. [Lists and Tuples](lessons/lists.md)
