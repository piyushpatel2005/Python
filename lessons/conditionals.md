# Conditionals

Python supports conditionals like if... else, if else if like other languages although it is little different in Python.

```python
if condition:
  ... indented statements
  ... .. ..
elif condition2:
  .... statements2
else:
  statements3...
```

[Conditional example](examples/conditional.py)

Python uses following relational operators in conditions.

== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

It also uses **Logical operators** to refine conditions.

| Operator | Name |
----------|:-------:|
|and     | AND |
|or    | OR |
|not    | NOT |

```python
if age >= 65 and age <= 30:
  ...
```

- Conditional operators return Boolean output "True" or "False".
- You can nest if else to make complex selection.
