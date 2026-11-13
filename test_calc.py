import unittest

from calc import Calc


class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.calc=Calc()
        result=self.calc.add(1,2)
        self.assertEqual(3,result)
