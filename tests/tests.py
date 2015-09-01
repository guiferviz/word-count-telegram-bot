

import unittest

from google.appengine.ext import testbed


class Tests(unittest.TestCase):

    """ Test for test """
    def setUp(self):
        # Create and activate testbed
        self.testbed = testbed.Testbed()
        self.testbed.activate()

    def test1(self):
        pass

    def tearDown(self):
        self.testbed.deactivate()
