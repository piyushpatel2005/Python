import unittest
from test_mymath import TestAdd


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    # makeSuite turns test case into TestSuite
    suite.addTest(unittest.makeSuite(TestAdd))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


my_suite()
