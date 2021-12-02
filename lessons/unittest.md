# Unittest module

Unittest is a testing framework that originally inspired JUnit. The unittest frameworks support following.
- **Test Fixture**: A fixture is what is used to setup a test so it can be run and also tears down when the test is finished. 
- **TestCase**: The test case is actual test. It will typically check that a specific response comes from a specific set of inputs. It provides a base class `TestCase` that can be used to create new test cases.
- **Test Suite**: It is a collection of test cases, test suites or both.
- **Test Runner**: A runner is what controls or orchestrates  the running of tests or suites.

Example [math](../examples/testing/mymath.py) module and its testcases in [test_mymath](../examples/testing/test_mymath.py). For unittesting, each method begins with the lettter "test". It tells the test runner which methods are tests and it should run. You can execute tests using `python test_mymath.py` or `python test_mymath.py -v`.

We can check different options for unit testing using `-h` command line option like `python test_mymath.py -h`. We can execute specific method using `python -m unittest test_mymath.TestAdd.test_add_integers`.

Let's take a look at [database testing example](../examples/testing/test_simple_db.py)

**TestSuite** is a collection of test cases, test suites or both. Usually `unittest.main()` will make sure to gather all module's test cases before executing them. For more control, we can use `TestSuite` class.

Check an [example of test suite](../examples/testing/test_suite.py)

If we want to skip any test, we can use `@unittest.skip` decorator. To conditionally skip a test, use `@unittest.skipUnless` as shown in [test_mymath module](../examples/testing/test_mymath.py). There is also `skipIf` which will skip the test if the condition is True. Check by executing this script as `python -m unittest test_mymath.py -v`.

The unittest module can be used with doctest module. If you have many modules with doctests, you will want to be able to run them systematically. The unittest module supports Test Discovery which allows unittest to look at the contents of a directory and determine from the filename which ones might contain tests. It then loads the test by importing them.
For examples, [check](../examples/testing/test_discovery/test_doctests.py). We can execute this module using `python -m unittest discover -v`.

## Mocking

The unittest module includes a `mock` submodule which allows you to replace portions of the system that you are testing with mock objects as well as make assertions about how they were used. This is useful for simulating system resources that aren't available in your test environment. One good example for this mocking is for third party services like Twitter or Facebook. We don't want to fetch tweets or retweet for testing. Another good example if you have a tool for making updates to database tables. Instead of doing any of these in tests, you can use mock. It will allow to mock and stub out those kinds of side-effects so you don't have to worry about them. Instead of interacting with the third party resources, you will be running your tests against a dummy API that matches those resources. Your application is calling the functions it's supposed to. You don't care about anything else.

Python mock class can mimic other Python class. This allows to examine what methods were called on your mocked class and even what parameters were passed to them. Check a very [simple mock example](../examples/testing/test_simple_mock.py). In this we create instance of `Mock` class and set the mock object's `__str__` method to 'Mocking' value. 

The mock module supports few asserts. Check an [example](../examples/testing/test_mock_asserts.py) file.
We can also create side effects of mock objects via the `side_effect` argument. A side effect is something that happens when you run your function. For example, some videogames have integration into social media. When you score a certain number of points, win a trophy, complete a level or some other goal, it will record it and also post about it to Twitter, Facebook or anything else. Let's see [an example of side effects](../examples/testing/test_side_effects.py). In this example, it's pretending to update a database. You can also make side effect raise an exception if you want to.

The mock submodule also supports *autospeccing*. The autospec allows to create mock objects that contain the same attributes and methods of the objects that you are replacing with you mock. They will even have the same call signature as the real object. This can be created using `create_autospec` function or by passing in the `autospec` argument to mock library's `patch` decorator. [Here](../examples/testing/test_autospec.py) is an example of this.

The mock module has a little function called `patch` that can be used as a function decorator, a class decorator or even a context manager. This allows us to create mock classes or objects in a module that you want to test as it will be replaced by a mock. I've a [webreader](../examples/testing/webreader.py) which reads from a url and return html text. If we are building web crawler, we don't want to download and read GBs of data. We can use mocked version of `urllib` so that we can call function without actually downloading anything. We have create a [mock webpage reader](../examples/testing/mock_webreader.py). In this case, we are mocking `urllib.request.urlopen` function and we call `read_webpage` function with Google URL. If you run this `python mock_webreader.py`, we get a MagicMock object.

Let's see bigger example. I've created [my_module](../examples/testing/my_module.py) and the [corresponding tests](../examples/testing/test_my_module.py).


**coverage.py** is 3rd party tool for Python for measuring code coverage. To install this tool, use pip

```shell
pip install coverage
```

To see the coverage, we have to first run the coverage on a test file.

```shell
cd examples/testing
coverage run test_mymath.py
coverage report -m # show coverage report. `-m` shows missing column in output
coverage html # create htmlcov folder and put index.html with coverage report.
```

`coverage.py` supports configuration through classic `.ini` files. We can specify what source files we want it to analyze. We can also specify `-include` or `-omit` to include a list of file name patterns or to exclude pattern.

