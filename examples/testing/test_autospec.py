from unittest.mock import create_autospec


def add(a, b):
    return a + b


mocked_func = create_autospec(add, return_value=10)
print(mocked_func(1, 2))  # 10

mocked_func(1, 2, 3)  # TypeError
