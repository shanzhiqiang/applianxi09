import pytest,os,yaml,sys
sys.path.append(os.getcwd())
from Base.base import GetData


def get_sum_list():
    result = []
    data = GetData().get_yml_data("sum.yaml")
    for i in data.values():  #i = {a:1,b:2,c:3}
        result.append(tuple(i.values()))  # =  [1,2,3]
    return result

class TestSum:

    @pytest.mark.parametrize("a,b,c",get_sum_list())
    def test01(self,a,b,c):
        print("{}+{}={}".format(a,b,c))
        assert a + b == c