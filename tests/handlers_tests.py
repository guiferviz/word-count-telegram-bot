

from webtest import app

import test_suite


class HandlersTests(test_suite.AppEngineTestBase):

    def test1(self):
        try:
            self.testapp.get('/')
            raise Exception('No 404 error asking for "/"')
        except app.AppError as error:
            self.assertTrue('404 Not Found' in error.message)
