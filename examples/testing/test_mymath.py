import mymath
import unittest


class TestAdd(unittest.TestCase):
    """
    Test the add function from mymath library
    """

    def test_add_integers(self):
        """
        Tests that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    @unittest.skip('Skip this test')
    def test_add_strings(self):
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

    # @unittest.skipUnless(sys.platform.startswith("win"), "requires windows")
    def test_adding_on_windows(self):
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract_integers(self):
        result = mymath.subtract(10, 8)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
