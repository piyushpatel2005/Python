# Object Oriented Programming

Here, the comparison of Java and Python makes it easy to understand the constructs of Python language.

Class is defined using `class` keyword. It has __init__ method which creates an object from the class and initializes its attributes (like constructor in Java).

Object is an instance of a class. The object has an identity (a unique address), a state(the data that it stores), and behavior(the methods).

OOP groups related variables and functions into data structures called objects.

```python
class Product:
  # constructor that initializes 3 attributes
  def __init__ (self, name, price, discount):
    self.name = name
    self.price = price
    self.discount = discount

  def getDiscountAmount(self):
    return self.price * self.discount / 100
```

How to use objects

```python
from objects import Product
product1 = Product("Stanley 13", 12.99, 3)
print("Name: {:s}".format(product1.name))
```

- All methods including constructor, must take a reference to the object self as the first argument.
- For OOP, usually camel case is used.
- `__init__()` method can be used to initialize attributes of the object.

```python
def __init__(self):
  self.name = ""
  self.price = 0.0
  self.discount = 0
```

```python
def __init__(self, name="", price="0.0", discount=0):
  self.name = name
  self.price = price
  self.discount = discount
```

[Product Viewer OOP Example](../examples/product_viewer.py)

## Composition

a way to combine simple objects into more complex data structures. In composition, one object will contain another object.

[Composition for Dice using Die](../examples/dice.py)

[How to work with composite objects](../examples/dice_roller.py)

## Encapsulation

Encapsulation allows you to prevent direct access to data attributes of an object. Also known as Data hiding.
In Python, you can make an attribute private by beginning attribute name with two underscores. Then we provide a public method to get and set an attribute.

Another way is to provide private attribute using double underscore and then public property without underscores.

An *interface* allows programmer to use an object without understanding its internal code.

```python
class Die:
  def __init__(self):
    self.__value = 1

  def getValue(self):
    return self.__value

  def roll(self):
    self.__value = random.randrange(1, 7)
```

Now if you try to access value attribute like this:

```python
die = Die()
die.__value = 10
```

it gives an `AttributeError: 'Die' object has no attribute '__value'`

You can get the value using `die.getValue()` method.

To access the hidden attribute, you also need to specify `setValue()` method.

```python
class Die:
  def __init__(self):
    self.__value = 1

  def getValue(self):
    return self.__value

  def setValue(self, value):
    if value < 1 or value > 6:
      raise ValueError("Die value must be from 1 to 6.")
    else:
      self.__value = value

  def roll(self):
    self.__value = random.randrange(1,7)
```

```python
die = Die()
die.setValue(6)
print("Die:",die.getValue())
```

Python also provides property to access private attributes easily. To create a property, we can use special language feature known as an annotation. To designate a method for getting a property, you code the `@property` annotation just above the method definition. To designate a method for setting a property, you code the `@sign` followed by a period and a word setter.

```python
class Die:
  def __init__(self):
    self.__value = 1

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, value):
    if value < 1 or value > 6:
      raise ValueError("Die value must be from 1 to 6.")
    else:
      self.__value = value
```

```python
die = Die()
die.value = 6
print("Die:", die.value)
```

- `@property` : coded above the getter method for the property
- `@propertyName.setter` : coded above the setter method for the specified property

If you set only setter method for a property, it becomes write-only property. If the class doesn't provide a setter method for the value property, it becomes read-only property.

When you use list, if you return list using read-only property, this returned list can be modified. To prevent that list can be converted to tuple which is immutable. Then it returns the tuple to the calling code. This implements encapsulation for lists.

**Modified Dice and Die classses**

```python
import random

class Die:
  def __init__(self):
    self.__value = 1

  @property
  def value(self):        # read only
    return self.__value

  def roll(self):
    self.__value = random.randrange(1,7)

class Dice:
  def __init__(self):
    self.__list = []

  @property
  def list(self):           # read only
    dice_tuple = tuple(self.__list)
    return dice_tuple

  def addDie(self, die):
    self.__list.append(die)
```

With Python, you can wait until you find real need to implement Encapsulation. However, if you do need to implement, you can simply create property and the interface won't be changed as it is accessed the same way as a public attribute. With other languages, you have to implement it from the beginning or else change the interface to use setter and getter methods.

```python
die.value = 1
print(die.value)
```

```python
class Product:
  def __init__(self, name="", price=0.0, discount=0):
    self.name = name    # public
    self.price = price    # price is set using property to use validation in the setter method.
    self.discount = discount    # public

  @property
  def price(self):
    return self.__price

  @price.setter
  def price(self, price):
    if price < 0:
      raise ValueError("Price can't be less than 0")
    else:
      self.__price = price

  def getDiscountAmount(self):
    return self.price * self.discount / 100

  def getDiscountPrice(self):
    return self.price - self.getDiscountAmount()
```

```python
product = Product()
product.price = -11.50    # ValueError: Price can't be less than 0
```

[Game using OOP](../examples/pig_dice/pig_dice.py)
