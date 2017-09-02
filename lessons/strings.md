# Working with Strings

Strings are immutable, so if you try to assign a new character to a string index, it will throw TypeError.

- `ord(char)` : returns integer (ordinal) values for unicode character.
- `len(str)` : returns length of the string

To slice a string you can use the same syntax as lists.

```python
message = "Hello out there!"
message[:5] # 'Hello'
message[10:]  # 'there!'
print("=" * 20) # prints '=' 20 times.
```

You can also use triple quotes to create a multiline string

```python
query = '''SELECT ceategoryID, name
           FROM Category WHERE categoryID = ?'''
```

If you use an index that doesn't exist in the string, Python raises IndexError

- To find if the word or character exists in a string.

```python
message = "Hello, Piyush! How are you?"
"Hello" in message  # True
"hello" in message  # False
```

Loop through string

```python
for char in message:
  print(char)
```

**Methods of string object**

- `isalpha()` : True if all characters are alphabetic
- `islower()` : True if all characters lowercase
- `isupper()` :
- `isdigit()` : if all characters are digits
- `startswith(str)` : if the string starts with str
- `endswith(str)` : if ends with
- `lower()` : convert to lowercase
- `upper()` : convert to uppercase
- `title()` : converts to title case
- `lstrip()` : strip whitespace from the left and return the string.
- `rstrip()` : right strip
- `strip()` : strips whitespace from both sides
- `ljust(width)` : returns left justified string with spaces added.
- `rjust(width)` : right justified string
- `center(width)` : center align

```python
print("Hammer".ljust(14), "$9.99".rjust(10))
```

- `find(str[, start][,end])` : finds specified string and returns index of the first occurence starting from start index and ending at this given end index. If not found, returns -1.
- `replace(old, new[, num])` : returns string with old substring replaced by new substring for specified number of occurrences.

```python
email = example@example.com
at_index = email.find("@")
dot_index = email.find(".", at_index)

if at_index == -1 or dot_index == -1:
  print("Invalid email address:", email)
```

[Create account example](../examples/create_account.py)

- `split([delimiter][, num])` : uses delimiter to split a string into substrings and returns a list of those substrings. Default delimiter is space.

```python
date = "11/9/1972"
date = date.split("/")
month = int(date[0])
day = int(date[1])
year = int(date[2])
year = int(date[8]) # IndexError
```

- `join(sequence)` : joins the elements of sequence into a string that uses the current string as the delimiter.

```python
address = ["Gujarat", "India"]
address = ", ".join(address)
print(address)    # Gujarat, India
```

[Word Count program](../examples/word_count.py)
