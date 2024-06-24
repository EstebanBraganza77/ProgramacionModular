import unittest
from tests.test_pec4 import TestReadClean, TestProcess, TestGroup


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReadClean))
    suite.addTest(unittest.makeSuite(TestProcess))
    suite.addTest(unittest.makeSuite(TestGroup))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())