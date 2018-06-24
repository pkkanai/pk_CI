# coding:utf-8

import unittest
from fuga import Fuga

class HogeTest(unittest.TestCase):

    #def setUp(self):
    #    print('setUp')

    def test_first(self):
        print('うんこしたい')

    def test_first(self):
        print('はんまーかんまー')
        True
        print(1+1)


    def test_fuga(self):
        fuga = Fuga()
        self.assertTrue(fuga.index())


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite
