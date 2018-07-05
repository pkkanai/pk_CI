import unittest
from hoge import Hoge

class HogeTest(unittest.TestCase):

    #各テストセットアップ時のメッセージ
    def setUp(self):
        print('setup ok')
a = input('>>')
    #テスト1：文字出すだけ
    def test_first(self):
        print('テストofテスト')

    #テスト2：ほげのindexメソッド呼び出し
    def test_hoge(self):
        hoge = Hoge()
        self.assertTrue(hoge.index())


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite
