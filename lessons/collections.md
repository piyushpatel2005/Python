# Collections module

Collections module contains special data types which can be used to replace Python's general purpose containers. It also contains submodule called abc for Abstract Base classes.

## ChainMap

`ChainMap` provides the ability to link multiple mappings together such that they end up being a single unit.  It accepts `*maps` which means it will accept any number of mappings or dictionaries and turn them into a single view that you can update.

```python
from collections import ChainMap
car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print(car_pricing['hood'])
```

ChainMap instance is created by passing multiple dictionaries. If we try to access a key, the ChainMap will go through each map in order to see if that key exists and has a value. If it does, it will return the first value it finds for that key. This is useful for setting defaults. For example, our application has few defaults but if there is an environment variable with that key, it will override the defaults. We can also add arguments which will override environmental variables.

```python
import argparse
import os

from collections import ChainMap

def main():
    app_defaults = {'username': 'admin', 'password': 'admin'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    command_line_arguments = {key: value for key, value in vars(args).items() if value}

    chain = ChainMap(command_line_arguments, os.environ, app_defaults)
    print(chain['username'])

if __name__ == '__main__':
    main()
    os.environ['username'] = 'test'
    main()
```

In above example, command line arguments override environment variables which again override the app defaults.

## Counter

The collections module also provides Counter which helps us tally any iterables.

```python
from collections import Counter
print (Counter('superfluous'))
# Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})

counter = Counter('superfluous')
print(counter['u']) # returns how many times 'u' occurs in superfluous
```

The Counter provides few methods that may be useful.

```python
print(list(counter.elements())) # provides list of each elements
# ['u', 'u', 'u', 's', 's', 'e', 'l', 'f', 'o', 'r', 'p']
# get top 2 most recurring items
print(counter.most_common(2)) # [('u', 3), ('s', 2)]

counter_one = Counter("superfluous")
print(counter_one)
# Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})
counter_two = Counter('super')
print(counter_one.subtract(counter_two)) # None, it subtracts elements of counter_two
print(counter_one)
# Counter({'u': 2, 's': 1, 'e': 0, 'l': 1, 'f': 1, 'o': 1, 'r': 0, 'p': 0})
```

## defaultdict

The defaultdict is a subclass of Python's dict that accepts default_factory as primary argument. We can also use int, list or  a lambda function for this default_factory. This pattern helps simplify some code. Below examples will clarify these.

```python
# calculate occurences of each word in dictionary
sentence = "Brown fox bites the brown dog"
words = sentence.split(' ')
d = {}
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)
```

The same could be easily written usind defaultdict as below.

```python
from collections import defaultdict
sentence = "Brown fox bites the brown dog"
words = sentence.split(' ')
d = defaultdict(int)
for word in words:
    d[word] += 1
print(d)
```

Another example, where we want to assign multiple transactions to accounts in the form of lists.

```python
my_list = [(123, 100.23), (234, 234.32), (123, 10.23), (332, 192.23)]
d = {}
for acct_num, amount in my_list:
    if acct_num in d:
        d[acct_num].append(amount)
    else:
        d[acct_num] = [amount]
print(d)
```

```python
#defaultdict implementation
from collections import defaultdict
my_list = [(123, 100.23), (234, 234.32), (123, 10.23), (332, 192.23)]
d = defaultdict(list)
for acct_num, amount in my_list:
    d[acct_num].append(amount)
print(d)
```

We can also use lambda to default specific type of default values. Here, defaultdict will assign 'Cat' as the default value for any key. This way, it's impossible to cause a `KeyError`. 

```python
from collections import defaultdict
animal = defaultdict(lambda: 'Cat')
animal['Sam'] = 'Tiger'
print(animal['Julie']) # Cat
```

However, `KeyError` is possible if we create a defaultdict of `None`.

```python
from collections import defaultdict
x = defaultdict(None)
print(x['Mike']) # KeyError
```

## deque

Deques are generalisation of stacks and queues. Deques are thread-safe and support memory efficient appends and pops from either side of the deque. A list is optimized for fast fixed-length operations. A deque accepts a `maxlen` argument which sets the bounds for the deque otherwise the deque will grow to an arbitrary size. When bounded deque is full, any new items added will cause the same number of items to be popped off the other end. In general, for fast appends and fast pops, use deque. If you need fast random access, use list. To create a deque, we need to pass an iterable.

```python
from collections import deque
import string
d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)
d.append('bork')
d.appendleft('test')
d.rotate(1) # rotate clockwise all elements by one position
```

```python
from collections import deque

def get_last(filename, n=5):
    """
    Returns the last n lines from the file like Linux `tail` command.
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print("Error opening file: {}".format(filename))
        raise
```

Here deque is bounded to `n`. So, it will finally have only last `n` lines.

## NamedTuple

Namedtuple can be used to replace Python's tuple. It can be used like a struct from other languages.

```python
from collections import namedtuple

Parts = namedtuple('Parts', 'id desc cost amount') # space delimited list of properties
auto_parts = Parts(id='123', desc='Ford Engine', cost=1231.99, amount=19)
print(auto_parts.id) # 123
print(auto_parts[2]) # 1231.99
id, desc, cost, amount = auto_parts # extract elements of namedtuple
```

We can also convert a python dictionary into an object like structure.

```python
from collections import namedtuple
Parts = {'id': '123', 'desc': 'Ford Engine', 'cost': 1231.99, 'amount': 19}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print(parts) # Parts(amount=19, id='123', desc='Ford Engine', cost=1231.99)
```

## OrderedDict

In `OrderedDict`, the dictionary keeps track of the order of the keys as they are added. In regular Python dictionary, this order is not maintained. For example, if we had a situation where we wanted keys to be in sorted and then iterate through them, we can write them like below snippets.

```python
keys = d.keys()

keys = sorted(keys)

for key in keys:
    print(key, d[key])
```

The same can be achieved with OrderedDict.

```python
from collections import OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
for key in new_d:
    print(key, new_d[key])
```

`OrderedDict`s have `popitem` which will return and remove a (key, item) pair. There is `move_to_end` method which will move an existing key to either end of the `OrderedDict` depending on whether the last argument for `OrderedDict` is set to `True` (default) or `False`.
For reverse iteration of key, value pairs, we can use `reversed` function.

```python
for key in reversed(new_d):
    print(key, new_d[key])
```
