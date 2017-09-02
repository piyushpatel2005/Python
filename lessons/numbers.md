# Working with Numbers

Python provides different modules to work with numbers.

## Math Module

Math module has many constants and functions for working with numbers.

- pi : the value of pi to 15 decimal positions
- `pow(num, pow)` : raises the number to specified power
- `sqrt(num)` : square root
- `ceil(num)` : rounds the float number up to nearest int
- `floor(num)` : rounds the float number down to nearest int

```python
import math as m
result = m.pow(2, 3)
radius = 12
circumference = m.pi * radius * 2
area = m.pi * m.pow(radius, 2)
result = m.floor(12.54) # 12
result = m.ceil(12.2) # 13
```

# Formatting output

String format() method can be used to format the output.

```python
fp = 12345.6789
print("{:.2f}".format(fp))  # 12345.67
print("{:,.2f}".format(fp)) # 12,345.67
i = 12345
print("{:,d}".format(i)) # 12,345
print("{:.2e}".format(fp))  # 1.23e+04
print("{:.1%}".format(fp)) # 12.3%
print("{:15} {:10.2f} {:5d}".format("Nails", 14.5, 10)) # Make right justified
print("{:15} {:>10} {:>5}".format("Hammer"< 9.99, 3)) # left justified float and int numbers.
```

## Locale module

It is used for formatting numbers in various countries.

- setlocale(category, locale) : sets locale for the specified category. Category can be LC_ALL, LC_MONETARY or LC_NUMERIC. It locale string is empty, it attempts to set the locale to the user's default locale.
- currency(num[, grouping]) : returns the specified number formatted as currency. If grouping set to True, the number includes thousands separator.
- format(format, num[, goruping]) : returns specified number formatted for the current locale. If grouping set to True, the number includes thousands separator.

```python
import locale as lc
lc.setlocale(lc.LC_ALL, "us")   # works with Windows system
lc.setlocale(lc.LC_ALL, "en_US")  # works with Mac Systems
print(lc.currency(12345.15, grouping=True)) # $12,345.15 for US
print(lc.format("%d", 12345, grouping=True))  # 12,345
print(lc.format("%.2f", 12345.67, grouping=True)) # 12,345.15
```

When working with floating point numbers, you need to keep floating number to 2 decimal digits. To do that, you can use round() function of Python.

```python
discount = round(order_total * discount_percent, 2)
sales_tax = round(subtotal * 0.05, 2)
```

## Decimal module

When working with decimal digits, round() functions can be used but Python provides decimal module which makes it even easier. Decimal numbers are exact values unlike floating point numbers. For this we use Decimal class of decimal module.

You cannot mix decimal number with floating point numbers while doing arithmatic operations. For rounding with decimal numbers, we can use quantize() method. This method uses ROUND_HALF_EVEN to round the numbers evenly means 10.005 will become 10.00. We can also use ROUND_HALF_UP to make 10.005 to 10.01.

```python
from decimal import Decimal, ROUND_HALF_UP
order_total = Decimal("100.05")
discount_percent = Decimal(".1")
discount = order_total * discount_percent # 10.005

subtotal = order_total - discount # 90.045
tax_percent = Decimal("0.05")
sales_tax = subtotal * tax_percent  # 4.50225
invoice_total = subtotal + sales_tax

test1 = subtotal * 2  # legal, mixing with int and Decimal
test2 = subtotal * 3.5  # illegal, can't mix Decimal and float

discount = Decimal("10.005")
discount = discount.quantize(Decimal("1.00")) # 10.00
discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)  # 10.01

```

We can also calculate multiplication, division and other operations with Decimal numbers.

[Invoice program with Decimal numbers](../examples/invoice.py)
