import unittest
from tests.test_read_clean import TestReadClean, TestProcess


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReadClean))
    suite.addTest(unittest.makeSuite(TestProcess))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())