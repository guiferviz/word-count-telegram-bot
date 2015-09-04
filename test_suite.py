

import logging
import os
import unittest
import webtest

import dev_appserver

# Fix the sys.path to include GAE extra paths.
dev_appserver.fix_sys_path()

from google.appengine.ext import testbed

import main


# Folder where test will be search.
TEST_DIR = os.path.join(os.path.dirname(__file__), 'tests')


class AppEngineTestBase(unittest.TestCase):
    """
    Base class for AppEngine tests.
    """

    def setUp(self):
        # Create and activate Testbed to moock AppEngine APIs.
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        # Create app for testing handlers.
        self.testapp = webtest.TestApp(main.app)
        # Not showing logging.
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        self.testbed.deactivate()


def runAllTests():
    """
    Run all tests.
    """
    loader = unittest.TestLoader()
    test_suite = loader.discover(TEST_DIR, pattern='*')
    unittest.TextTestRunner(verbosity=2).run(test_suite)


# If it's the main file we run all the tests under 'tests' module.
if __name__ == '__main__':
    runAllTests()
