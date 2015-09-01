

import os
import unittest

import dev_appserver


# Fix the sys.path to include GAE extra paths.
dev_appserver.fix_sys_path()

# If it's the main file we run all the tests under tests module.
if __name__ == '__main__':
    loader = unittest.TestLoader()
    test_suite = loader.discover(os.path.dirname(__file__))
    unittest.TextTestRunner(verbosity=2).run(test_suite)
