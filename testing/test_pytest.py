# -*- coding: utf-8 -*-
import os
from pathlib import Path
import pytest
import yaml
from python.calc import Calc
from decimal import Decimal

now_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 获取到项目的根目录位置
dir_path = Path(now_path, "./datas")  # 当前文件位置 拼装 Logs 形成工作目录
log_path = dir_path.resolve()   # 返回文件路径

class TestCalc:

    def setup(self):
        self.calc = Calc()

    @pytest.mark.run(order=3)
    def test_zadd(self):
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result

    @pytest.mark.parametrize('a, b, expect', [[1, 2, 3], [0.1, 0.2, 0.3], [10, 20, 30]])
    def test_add_1(self, a, b, expect):
        try:
            result = self.calc.add(Decimal(a), Decimal(b))
            print(result)
            assert result == expect
        except TypeError:
            return print("类型错误")


    @pytest.mark.parametrize('a, b, expect',
                             yaml.safe_load(open(f"{log_path}\\add.yaml")))
    def test_add_2(self, a, b, expect):
        try:
            result = self.calc.add(Decimal(a), Decimal(b))
            print(result)
            assert result == expect
        except TypeError:
            return print("类型错误")

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open(f"{log_path}\\sub.yaml")))
    def test_sub(self, a, b, expect):
        try:
            result = self.calc.sub(Decimal(a), Decimal(b))
            print(result)
            assert result == expect
        except TypeError:
            return print("类型错误")

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open(f"{log_path}\\take.yaml")))
    def test_take(self, a, b, expect):
        try:
            result = self.calc.take(a, b)
            print(result)
            assert result == expect
        except TypeError:
            return print("类型错误")

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open(f"{log_path}\\div.yaml")))
    def test_div(self,  a, b, expect):
        try:
            result = self.calc.div(Decimal(a), Decimal(b))
            print(result)
            assert result == expect
        except TypeError:
            return print("类型错误")


if __name__ == "__main__":
    pytest.main(['-vs', 'test_pytest.pyTestCalc::test_add_1'])