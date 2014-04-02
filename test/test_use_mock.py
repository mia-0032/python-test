# -*- coding:utf-8 -*-

import unittest

class SideEffectTestResult(object):
    """side_effectの返り値用
    """
    pass


class CalculationModelTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def dataProvider(self, param_1, param_2):
        # 返り値を置き換える関数と同じ数の引数でないといけない。
        return SideEffectTestResult()

    def test_execute_1(self):
        """Mockインスタンスに置き換えてのテスト
        """
        mock_dao = Mock()  # Mockの作成
        # findメソッドとその返り値を作成
        mock_dao.find.return_value = 'testtest'
        # テスト対象のインスタンスを作成
        test_obj = CalculationModel(mock_dao)
        # 返り値が変わっていることを確認。
        self.assertEqual('testtest', test_obj.execute())
        # findメソッドが1回呼ばれていることを確認。
        self.assertEqual(mock_dao.find.call_count, 1)
        # メソッドが呼ばれたときの引数を取得できる
        # 0番から呼ばれた順に格納されている
        # callオブジェクトに格納されるのでlist化
        # 配列の0番目にタプルで引数、1番目に辞書でキーワード引数が格納される
        self.assertEqual(list(mock_dao.find.call_args_list[0]),
                         [('hoge',), {'param_2': 'foo'}])

    def test_execute_2(self):
        """メソッドをMockインスタンスに置き換えてのテスト
        """
        HogehogeDao.find = Mock(return_value='method_mock_test')
        dao = HogehogeDao()
        test_obj = CalculationModel(dao)
        self.assertEqual('method_mock_test', test_obj.execute())

    def test_execute_3(self):
        """with構文とpatch()を使って置き換えてのテスト
        """
        with patch('__main__.HogehogeDao') as mock_dao:
            mock_dao.find.return_value = 'with_mock_test'
            test_obj = CalculationModel(mock_dao)
            self.assertEqual('with_mock_test', test_obj.execute())

    def test_execute_4(self):
        """side_effectを使ってメソッドを返り値にする
        """
        mock_dao = Mock()
        mock_dao.find.side_effect = self.dataProvider
        # テスト対象のインスタンスを作成
        test_obj = CalculationModel(mock_dao)
        # 返り値が変わっていることを確認。
        self.assertIsInstance(test_obj.execute(), SideEffectTestResult)

unittest.main()
