# Taking input from the user and printing output

Variables can be created on the fly in Python.

```python
input = 3
str_input = "Hello"
```

Strings are represented with double quotes or single quotes. However, it must end with the same kind of quotes.
You can escape the single quote or double quote using:

```python
input = "Hi, This is Dog's tail."
input = 'Hi, This is Dog\'s tail.'
```

You can take user input using:

```python
user_choice = input("Enter your selection: ")
```

The input() function takes string as input even if the user enters integer. To convert the input to integer, use int().

There are three data types in Python: int, float and str.

You can use print() function to print to the screen.

```python
print(msg, end="\n", sep=" ")
```

You can change the separator and end named parameters to change the behaviour of the print() function.

You can print multiple arguments using string.format
