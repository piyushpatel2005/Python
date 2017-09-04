# Inheritance

Inheritance allows you to create a new class that's based on an existing class. When inheritance is used, subclass inherits the public attributes and methods of a super class.
Super class is also called *base* or *parent* class and subclass is also called a *derived* or *child* class.

To indicate that the class is a subclass, follow the name of the class by parentheses with superclass name inside parentheses.

You can also override methods from the super class and add new attributes to class with a constructor to initialize them.

When you override a method, it is sensible to call superclass method first so that if you change super class implementation, the same is reflected in the subclasses.

```python
class Product:
  def __init__(self, name="", price=0.0, discount=0):
    self.name = name
    self.price = price
    self.discount = discount

  def getDiscountAmount(self):
    return self.price * self.discount / 100

  def getDiscountPrice(self):
    return self.price - self.getDiscountAmount()

  def getDescription(self):
    return self.name
```

```python
class Book(Product):
  def __init__(self, name="", price=0.0, discount=0, author=""):
    Product.__Init__(self, name, price, discount)   # call super class constructor to initialize common attributes.
    self.author = author

  def getDescription(self):
    return Product.getDescription(self) + " by " + self.author    # Python uses super class name to access super class methods, similar to super in Java
```

## Polymorphism

Polymorphism lets you treat objects of different types as if they were the same type by referring to a superclass that's common to the objects. This allows you to write generic code that's designed to work with a superclass.

Polymorphism will allow you to call the correct method based on the type of object.

```python
# Product class method
def getDescription(self):
  return self.name
```

```python
# Book class method which inherits from Product class
def getDescription(self):
  return Product.getDescription(self) + " by " + self.author
```

```python
# Movie class method only which overrides Product class method
def getDescription(self):
  return Product.getDesription(self) + " (" + str(self.year) + ")"
```

```python
from objects import Product, Book, Movie

def show_products (products):
  print("PRODUCTS")
  for product in products:
    print(Product.getDescription())
  print()

def main():
  products = (Product("Rubber", 0.88, 3),
              Book("A book of tomorrow", 3.23, 2, "Michael Bay"),
              Movie("Independence Day", 9.99, 5, 2016))
  show_products(products)

if __name__ == "__main__":
  main()

# PRODUCTS
# Rubber
# A book of tomorrow by Michael Bay
# Independence Day (2016)
```

- `isinstance(object, [module.]className)` : returns True if the object is an instance of the specified class, otherwise False.

```python
from objects import Product, Book, Movie

def show_products(product):
  print("PRODUCT DATA")
  print("Name:", product.name)
  if isinstance(product, Book):
    product("Author:", product.author)
  if isinstance(product, Movie):
    print("Year:", product.year)
  print("Discount Price: {:.2f}".format(product.getDiscountPrice()))
  print()
```

[Product Viewer Example with inheritance and polymorphism](../examples/product_viewer/product_viewer.py)

In Python 3, a class named *object* is the superclass for all classes. You can override several methods of object class.

### Define String representation

- `__str__(self)` : to define string representation of an object.

```python
# __str__() method in Product class
def __str__(self):
  return self.name + " | " + str(self.price) + "|" + str(self.discount)
```

```python
# Code that uses string representation
product = Product("Laptop", 399.99, 12)
print(product)
# Laptop | 399.99 |12
```

The default `__str__()` method gives output like this:

`<objects.Product object at 0x03769930>`

### Define iterator for object

When we use `for obj in objects`, Python calls the `__iter__()` and `__next__()` methods to initialize the loop to get th enext objet in sequence of objects. So, if your object contains multiple objects, you need to override these methods.

If you have completed iterating through all elements, it should throw `StopIteration()`. All methods with double underscores are used by Python internally.

```python
class Dice:
  def __init__(self):
    self.__list = []

  def __iter__(self):
    self.__index = -1
    return self

  def __next__(self):
    if self.__index >= len(self.__list) - 1:
      raise StopIteration()
    self.__index += 1
    die = self.__list[self.__index]
    return die
```

```python
for die in dice:
  print(die.value, end=" ")
```

If `__iter__()` method is not defined, then console will throw an error.

`TypeError: 'Dice' object is not iterable`

There are many other methods that you can implement to extend the class functionality and make it useful for other programmers.

# Create custom exceptions

It's usually good idea to create custom exception and throw that so that in case you change the implementation still the same error is thrown. Additionally, it doesn't reveal internals of the class as you can throw Error with custom message.

To create custom Error class, you have to extend one of the in-built exception classes.

```python
class DataAccessError(Exception):
  pass
```

Inheritance is used when (i) one object is a type of another object, (ii) both classes are part of the same logical domain, (iii) the subclass primarily adds features to the superclass.

Composition is a has-a relationship.

## Creating Object Oriented Design

Steps to designing object-oriented programs.

1. Identify data attributes
2. Subdivide each attribute into its smallest useful components
3. Identify the classes
4. Identify the methods
5. Refine the classes, attributes and methods.

Data attributes are subdivided so that you can rebuild it when necessary by concatenating the attributes.

[OOP Design: Shopping Cart](../examples/shopping/)
