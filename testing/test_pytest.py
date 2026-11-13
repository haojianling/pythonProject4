import pytest

from calc import Calc


class TestCalc:
    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        assert 3==result
    def test_div(self):
        self.calc = Calc()
        result = self.calc.div(2, 2)
        assert 1==result
if __name__ == '__main__':
    pytest.main(["-vs","test_pytest.py::TestCalc::test_div"])