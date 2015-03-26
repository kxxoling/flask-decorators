import unittest
import flask


class MainTestCase(unittest.TestCase):

    def setUp(self):
        app = flask.Flask(__name__)

        self.app = app

    def tearDown(self):
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MainTestCase))

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
