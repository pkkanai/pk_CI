# coding:utf-8

import unittest
from fuga import Fuga

class HogeTest(unittest.TestCase):

    #セットアップ時のメッセージ
#    def setUp(self):
#        print('setup ok')

    #テスト：文字出すだけ
    def test_of_test(self):
        print('テストのテスト')

    def test_first2(self):
        print(1+1)
        False


    def test_fuga(self):
        fuga = Fuga()
        self.assertTrue(fuga.index())


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite
