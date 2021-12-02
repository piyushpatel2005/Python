def add(a, b):
    """
    Return the addition of the arguments: a + b

    add (1,2)
    #3
    add (-1, 10)
    #9
    add ('a', 'b')
    #'ab'
    add(1, '2')
    #Traceback (most recent call last):
    #  File "test_simple_math.py", line 17, in <module>
    #    add(1, '2')
    #  File "test_simple_math.py", line 14, in add
    #    return a + b
    #TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
