""" test file """
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class SimpleTest(unittest.TestCase):
    """ simple test"""
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        """ test skipped """
        self.fail("shouldn't happen")

    def test_pass(self):
        """ test pass """
        self.assertEqual(10, 7 + 3)

        # def test_fail(self):
        #     self.assertEqual(11, 7 + 3)
