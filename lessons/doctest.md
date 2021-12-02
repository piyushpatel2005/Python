# Doctest Module

The doctest module will look at your code and determine if you have any text that looks like an interactive Python session. Doctest has three primary uses:
- Checking that a module's docstrings are up-to-date by verifying the examples in the docstrings execute correctly.
- Do regression testing using the interactive examples in the text
- Write tutorial documentation for your package or module. You can do this by adding lots of examples in your docstrings that show inputs and outputs.

Check [example usage](../examples/testing/simple_math.py). Here `testmod` function call will search all the docstrings in the module and try to run the examples that look like interpreter sessions. We can verify by using `python test_simple_math.py -v` or by commenting out `if` block and using `python -m doctest -v test_simple_math.py`.

The doctest module works by examining the docstrings in the module, from the module level to the function, class and method levels. It will not look at imported modules though. For most part, you can copy-paste an interactive console session in and doctest will work fine with it. The doctest will look for output following the final `>>>` or `...` line that contains code. Tracebacks usually contain exact file path and line numbers which change when developing. doctest is pretty flexible. You need the Traceback line and the actual Exception line to make the test pass.

The doctest module also allows to write interactive examples to a text file using ReStructuredText which is a common mark-up language. You can check an [example file for add function](../examples/testing/add.txt) and the [corresponding test](../examples/testing/test_mymath_doctest.py). Now if you execute `python test_mymath_doctest.py -v`, it will succeed.

The doctest module also comes with several option flags to control doctest's behaviour. One of the easiest ways to use an option flag is with a directive. A doctest directive is a special Python comment that follows an example's source code.  One popular option flag is to use the ELLIPSIS flag. This flag allows us to cut out part of the output and still pass the test. In the first example, we are creating 100 element list using ellipsis. In the second example, we create instance of `Dog` class but it will give different memory location each time, so we use ellipsis.

```python
"""
print(list(range(100))) # doctest: +ELLIPSIS
#[0, 1, ..., 98, 99]

class Dog: pass
Dog() #doctest: +ELLIPSIS
#<__main__.Dog object at 0x...>
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```


