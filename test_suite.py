

import os
import unittest

import dev_appserver


# Folder where test will search.
TEST_DIR = os.path.join(os.path.dirname(__file__), 'tests')

# Fix the sys.path to include GAE extra paths.
dev_appserver.fix_sys_path()


# Run all tests.
def main():
    loader = unittest.TestLoader()
    test_suite = loader.discover(TEST_DIR, pattern='*')
    unittest.TextTestRunner(verbosity=2).run(test_suite)


# If it's the main file we run all the tests under 'tests' module.
if __name__ == '__main__':
    main()
