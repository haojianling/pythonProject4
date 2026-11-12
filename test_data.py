import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a+b)
    # def test_data2(self):
    #     a=11
    #     b=20
    #     print(a+b)
    # def test_data3(self):
    #     a=12
    #     b=20
    #     print(a+b)