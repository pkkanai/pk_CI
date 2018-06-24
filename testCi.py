# coding:python
# なんかか計算式でもやるか

import unittest
from fuga import Fuga


class HogeTest(unittest.TestCase):

    def setUp(self):
        print('unko')

    def test_fuga(self):
        fuga = Fuga()
        self.assertTrue(fuga.index())


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite
