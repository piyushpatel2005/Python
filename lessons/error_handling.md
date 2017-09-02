# Exception Handling

In Python, we use try...except statement to handle exceptions.

You cover the block of code that is likely to cause exception. For example, taking input from the user and working with those data.

```python
try:
  statements
except [Exceptionname]:
  statements
```

```python
try:
  number = int(input("Enter an integer: "))
  print("You entered a valid integer of " + str(number))
except ValueError:
  print("You entered an invalid integer. Please try again")
print("Thanks!")
```

You can also handle all exceptions, if you don't specify the type of exception in exception block.

```python
try:
  statements
except:
  # Handle all exceptions
  statements
```

[Exception Handling Retail Calculator example](../examples/retail_calculator.py)

When handling more than one error, the exceptions must be coded in sequence from the most specific to the most general exception.

Exception Hierarchy for file handling example:

- Exception
  - OSError
    - FileExistsError
    - FileNotFoundError
  - ValueError

```python
filename = input("Enter filename: ")
movies = []
try:
  with open(filename) as file:
    for line in file:
      line = line.replace("\n", "")
      movies.append(line)
except FileNotFoundError:
  print("Could not find the file named ", filename)
except OSError:
  print("File found - error reading file")
except Exception:
  print("An unexpected error occurred")
```

- `type(object)` : returns the class for the specified object.
- `exit()` : exits Python program

[Multiple Exception handling](../examples/multiple_exceptions.py)

[Movie List with Exception Handling](../examples/exception_handling_movie_list.py)

- After except clauses, a try statement can include finally clause. It is used to clean up the system resources. When you use with statement, you don't need it. File objects include special clean-up method.

```python
def read_movies(filename):
  try:
    file = open(filename, newline="")
    try:
      movies = []
      reader = csv.reader(file)
      for row in reader:
        movies.append(row)
      return movies
    except Exception as e:
      print(type(e), e)
    finally:
      file.close()
  except FileNotFoundError as e:  # try clause couldn't open file, so don't need to close file.
    print(e)
```

### How to raise an exception

For raising an exception, `raise` statement is used.

Syntax:

```python
raise ExceptionName("Error message")
```

```python
def get_movies(filename):
  try:
    with open(filename, newline="") as file:
      movies = []
      reader = csv.reader(file)
      for row in reader:
        movies.append(row)
    return movies
  except Exception as e:
    print(type(e), e)
```

Raise an exception that is handled by calling function

```python
def get_movies(filename):
  if len(filename) == 0:
    raise ValueError("The filename argument is required.")
  with open(filename, newline="") as file:
    movies = []
    reader = csv.reader(file)
    for row in reader:
      movies.append(row)
  return movies
```

Logging to a file

```python
try:
  with open(filename, newline="") as file:
    movies = []
    reader = csv.reader(file)
    for row in reader:
      movies.append(row)
  return movies
except Exception as e:
  log_exception(e)  # this function writes exception to the log file.
  raise e   # exception raised again so that calling function can handle it.
```
