# Lists and Tuples


## Lists:

data structure known as a sequence. Similar to array in other languages.

Syntax for creating a list

```python
mylist = [item1, item2, ...]
```

```python
temps = [48.0, 30.5, 20.2, 100.0, 42.0]
inventory = ["staff", "hat", "shoes"]
test_score = []  # empty list

# create list with n elements
scores = [0] * 5    # scores = [0. 0. 0. 0. 0]

scores[1] = 0   # accessing elements
```

**Functions for list**

- append(item) : appends item to the end of the list
- insert(index, item): inserts item at specified index.
- remove(item) : removes first item in the list that matches item specified. If not found, ValueError is thrown.
- index(item): returns index of the first occurence of specified item. If not found, ValueError.
- pop([index = len(list) - 1]): returns specified indexed item or the last item in the list.
- len(list) : returns the length of the list.

```python
inventory = ["staff", "hat", "robe", "bread"]
i = inventory.index("hat")
inventory.pop(i)
```

How to check whether an item is in a list

```python
inventory = ['staff', 'hat', 'bread']
item = 'bread'
if item in inventory:
  inventory.remove(item)
```

How to loop through list

```python
for item in list:
  statements
```

```python
nums = [1, 2, 3, 4]
for num in nums:
  print(num)
```

similar to

```python
i = 0
while i < len(nums):
  print(nums[i])
  i += 1
```

**Note:** When list is passed to a function, it is passed as reference. So, all the changes inside called functions will be made on the original list. You don't need to return list. List is mutable and str, int, float are immutable. Immutable data is passed by value.

[Example of list functions](../examples/list_example.py)

In Python, we can check whether an element exists in list using `in` operator.

```python
l = [1, 2, 'a']
print('a' in l)   # returns True
```


### List of Lists

A list element can contain another list making it 2D list. It is similar to 2D array.

Define list of lists

```python
movies = [["Titanic", 1997],
          ["Pearl Harbor", 2003]
         ]
```

Add to a list of lists

```python
# create inner list element
movie = []
movie.append("Guide")
movie.append(1978)
# add inner list element to outer list
movies.append(movie)
```

You can access each element using bracket notation. like movies[0][1] would return 1997.

Printing list of lists:

```python
for movie in movies:
  for item in movie:
    print(item, end=" | ")
  print()
```

**Other functions**

- list.count(item) : returns number of occurences of an item in the list.
- reverse(list): reverses the order of the items in the list.
- sort([key = function]): sorts the list items in place. key argument specifies the functions to be called on each item before sorting.
- sorted(list [,key=function]): returns a new list. Similar to sort function.
- min(list) : returns the minimum value in the list
- max(list): returns the maximum value in the list
- random.choice(list) : returns randomly selected item from the list
- random.shuffle(list) : shuffles the items in the list on a random basis

```python
nums = [5, 12, 2, 3, 2, 4]
count = nums.count(2)   # count = 2
nums.reverse()  # [12, 5, 4, 3, 2, 2]
nums.sort()   # [2, 2, 3, 4, 5, 12]

foodlist = ["orange", "apple", "Pear", "banana"]
foodlist.sort()   # ["Pear", "apple", "banana", "orange"] all uppercase letters come before lowercase
foodlist.sort(key=str.lower)  # ["apple", "banana", "orange", "Pear"]
min = min(nums)   # 2
```

When you assign a list to another variable, it creates a shallow copy. A change in one of the two lists will change another list.
To make a deepcopy, you can use, copy module's deepcopy() function.

```python
import copy
list_one = [1, 2, 3 ,4]
list_two = copy.deepcopy(list_one)
# Now two lists are identical but different.
```

- To **slice a list**, you can use:

```python
mylist[start=0[:end:step]]
```

```python
nums = [1, 2, 3, 4, 5]
nums[0:2]   # [1, 2]
nums[:2]    # [1, 2]
nums[3:]    # [4, 5]
nums[0:4:2] # [1, 3]
nums[::-1]  # [5, 4, 3, 2, 1]

# We can also add two lists to combine two list elements
inventory = ["staff", "rope"]
chest = ["scroll", "pestle"]
combined = inventory + chest   # ["staff", "rope", "scroll", "pestle"]
```

### List Comprehension

List comprehension allows us to create complex lists in single line of code. It is widely used in Data Science.

Here, we use lambda function to create list. You can't have complex logic in lambda functions. They are like arrow functions in JavaScript.

```python
my_list = [number for number in range(0,100) if number % 2 == 0]
# This creates a list with numbers between 0 and 100 which are even.
```

### Functional programming

Python has several functions that allow easy manipulation of lists using lambda functions.

```python
numbers = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, numbers))
# gives [-5, -4, -3, -2, -1]
```

Here filter function takes a function and the list as parameters.

`map` function is used to map the list to another list.

```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
```

`reduce` is used to sum all elements or get single value from list.

```python
from functools import reduce
product = reduce((lambda x,y: x*y), [1, 2, 3, 4, 5])    # returns 24
```


## Tuples:

tuples is sequence that works much like a list but they are immutable. They are created using parentheses.

**NOTE:** When you create a tuple with single item, you need to add comma at the end to indicate that this is tuple and not simple variable.

```python
scores = (99, )   # creates a tuple with single element
```

You can get items from tuple in variables by unpacking a tuple. You can also access individual elements using square bracket notation like lists.

A function can return tuple and the values can be unpacked in the calling function.

```python
tuple_values = (1, 2, 3)
x, y, z = tuple_values    # x = 1, y = 2, z = 3
x = tuple_values[2]
```

[Tuple example](../examples/number_crunch.py)
