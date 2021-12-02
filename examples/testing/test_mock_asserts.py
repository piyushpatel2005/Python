from unittest.mock import Mock


class TestClass():
    pass


cls = TestClass()
cls.method = Mock(return_value='mocking is fun')
cls.method(1, 2, 3)  # mocking is fun

cls.method.assert_called_once_with(1, 2, 3)
cls.method(1, 2, 3)  # mocking is fun

cls.method.assert_called_once_with(1, 2, 3)  # Failure
cls.other_method = Mock(return_value='Something else')
cls.other_method.assert_not_called()
