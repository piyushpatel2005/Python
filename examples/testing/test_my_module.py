import unittest
from my_module import MyClass, SomeOtherClass
from unittest.mock import patch, Mock


class TestMyModule(unittest.TestCase):

    # mock a method return specific value
    @patch.object(MyClass, 'my_method')
    def test_shouldReturnValue_whenMethodIsMocked(self, mock_my_method):
        mock_my_method.return_value = True
        some_other_class = SomeOtherClass()

        result = some_other_class.method_under_test()
        self.assertTrue(result)

    # mock an entire class
    @patch('my_module.MyClass')
    def test_shouldRecordMethodWasCalled_whenClassIsMocked(self,  mock_my_class):
        some_other_class = SomeOtherClass()
        some_other_class.method_under_test()
        self.assertTrue(mock_my_class.called)

    # mock entire class and set the return value of a method.
    # First, get the mock instance and then set the return of method of that mock instance.
    @patch('my_module.MyClass')
    def test_shouldReturnValue_whenReturnValueIsSetOnMethodOfMockedClass(self, mock_my_class):
        mc = mock_my_class.return_value
        mc.my_method.return_value = True
        some_other_class = SomeOtherClass()

        result = some_other_class.method_under_test()
        self.assertTrue(result)

    # To mock a method in a class with @patch.object but still return a different value each time it is called, use side_effect.
    # Side effects allow you to define a custom method and have that method called each time your mock method is called.
    # The return value from this method will be used as the return value of your mock method.
    @patch.object(MyClass, 'my_method')
    def test_shouldReturnANewValueEachTime_whenMethodIsMockedUsingSideEffect(self, mock_my_method):
        list_of_return_value = [True, False, False]

        def side_effect():
            return list_of_return_value.pop()

        mock_my_method.side_effect = side_effect
        some_other_class = SomeOtherClass()

        result_one = some_other_class.method_under_test()
        result_two = some_other_class.method_under_test()
        result_three = some_other_class.method_under_test()

        self.assertFalse(result_one)
        self.assertFalse(result_two)
        self.assertTrue(result_three)


if __name__ == '__main__':
    unittest.main()
