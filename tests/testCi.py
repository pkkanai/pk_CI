# coding:utf-8

import unittest
from fuga import Fuga

class HogeTest(unittest.TestCase):

    #各テストセットアップ時のメッセージ
    def setUp(self):
        print('setup ok')

    #テスト1：文字出すだけ
    def test_first(self):
        print('テストのテスト')

    #テスト2：ふがのindex呼び出し
    def test_hoge(self):
        go = 5
        fuga = Fuga()
        self.assertTrue(hoge.index(go))


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite
