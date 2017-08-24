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
