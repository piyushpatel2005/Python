# Argparse module

```python
# examples/argparser_1.py
import argparse
parser = argparse.ArgumentParser(
    description='A simple argument parser',
    epilog='Example usage'
)

parse.print_help()
```

if we call `python argparser_1.py`, it will print the help for the tool.

```python
import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is example usage"
    )
    return parser.parse_args()

if __name__ == '__main__':
    get_args()
```

Let's see how we can add few additional arguments.

```python
# examples/argparser_2.py
import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is example usage"
    )
    # required arguemnt
    parser.add_argument('-x', action='store', required=True, help='Help text for option x')

    # optional arguments
    parser.add_argument('-y', help='Help for option Y', default=False)
    parser.add_argument('-z', help = 'Help for option z', type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()
```

This time when we execute like `python argparser_2.py`, it will throw and error saying that `argument -x is required`.
If you execute like `python argparser_2.py -x something -y another -z 10`, it will print the arguments passed in Namespace object. If you want to pass short options and long options, you can add both like below example.

```python
parser.add_argument('-x', '--execute', action='store', required=True, help='Help for option x')
```

If we have an option that can be either or like either we can execute a program in verbose mode or without verbose logging, we can use `mutually_exclusive_group` function. For example, let's say option `-x` and `-y` are mutually exclusive, we can write it like this. With this, we have to make sure all mutually exclusive arguments are optional.

```python
import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is example usage"
    )
    # required arguemnt
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action='store', required=True, help='Help text for option x')
    group.add_argument('-y', help='Help for option Y', default=False)

    parser.add_argument('-z', help = 'Help for option z', type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()
```