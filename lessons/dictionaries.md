# Dictionary

Dictionary stores a colection of items. However, it is unordered. To create dictionary, you use curly braces({}). It is a key/value pair separated by colon(:). Dictionaries are accessed by a key that's typically a string but can be any immutable data type.

In some languages, dictionaries are called associative arrays. In some, they are called map.

```python
dictionary_name = {key1: value1, key2: value2, ...}
```

```python
countries = {
  "CA": "Canada",
  "IN": "India",
  "US": "United States"
}
numbers = {1: "One", 2: "Two", 3: "Three"}
country = counties['IN']  # country = "India"
```

If the key doesn't exist, a KeyError occurs.
We can check the key in dictionary using `in` keyword.

```python
code = "IN"
if code in countries:
  country = countries[code]
  print(country)
else:
  print("There is no country for this code: " + code)
```

- `get(key[, default_value])` : If specified key exists, this method returns its value. Otherwise, this method returns None or default value if it is supplied.

```python
country = countries.get("IN", "Unknown")  # Unknown
```

```python
code = "IE"
if code in countries:
  country = countries[code]
  del countries[code]
  print(country + " was deleted.")
else:
  print("There is no country for this code: " + code)
```

- To delete an item from the dictionary, you can use `del` keyword. You can also delete using pop() method of a dictionary. This returns the value for the specified key and deletes the key/value pair from the dictionary.
- `pop(key[, default_value])` : returns the value of the specified key and delets the key/value pair from the dictionary. The optional second argument is a value to return if the key doesn't exist.
- `clear()` : deletes all items.

```python
country = countries.pop("IN")
code = "NK"
country = countries.pop(code, "Unknown country")
print(country + " was deleted.")
countries.clear()
```

- `keys()` : returns a view object that contains all the keys in the dictionary.
- `items()` : returns a view object with tuple for each key/value pair in dictionary.
- `values()` : returns a view object that contains all the values in the dictionary.

## How to loop through keys and values

```python
for code in countries.keys():
  print(code + " : " + countries[code])
```

is equivalent to

```python
for code in countries:
  print(code + " : " + countries[code])
```

```python
for code, name in countries.items():
  print(code + " : " + name)
```

- To convert view object to a list, you can use list() constructor. To convert list of lists to dictionary, use dict() constructor. If any of the lists contain fewer or more than two values, the dict() constructor causes a ValueError that says the length of the sequence isn't correct.

- `list(view)` : converts the specified view object to a list
- `dict(view)` : converts specified 2D list or tuple to a dictionary.

```python
countries = {'IN': 'India', 'US': 'United States', 'CA', 'Canada'}
codes = list(countries.keys())
codes.sort()
for code in codes:
  print(code + " " + countries[code])
```

```python
countries = [['IN', 'India'], ['US', 'United States'], ['UK', 'United Kingdom']]
countries = dict(countries)
print(countries)
```

[View countries](../examples/countries.py)

Word counter:

```python
word_count = {}
for word in words:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
```

# Working with dictionary of dictionaries

```python
contacts = {
  "Piyush": {
    "first_name": "Piyush",
    "last_name": "Patel",
    "state": "Gujrat",
    "country": "India"
  },
  "Darshak": {
    "first_name": "Darshak",
    "last_name": "Shah",
    "state": "London",
    "country": "United Kingdom"
  },
  "Pritesh": {
    "first_name": "Pritesh",
    "last_name": "Patel",
    "state": "Gujarat",
    "country": "India"
  }
}

piyush_country = contacts['Piyush']['country']
email = contacts['Piyush']['email']   # KeyError
phone = contacts.get('Piyush', {}).get('email')   # None
phone = contacts.get('Piyush').get('email')   # None
phone = contacts.get('Ankit').get('first_name') # AttributeError
```

The value of the key can be complex data type such as another dictionary, a tuple or a list.
