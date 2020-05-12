# -*- coding: utf-8 -*-

import sys
sys.path.append('..')  # 把引入的包文件添加到系统环境变量中

import unittest
from python.calc import Calc

# print(sys.path)


class TestCalc(unittest.TestCase):

    def test_add_1(self):
        """测试 Add 相加方法"""
        self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        self.assertEqual(3, result)


unittest.main()
"""
if __name__ == "__main__":
    unittest.main()
同 unittest.main() 效果一致
"""






