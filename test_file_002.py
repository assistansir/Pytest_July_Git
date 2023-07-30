import pytest


class Test_credence_001:
    @pytest.mark.skip
    def test_mul_004(self):
        a=3
        b=7
        mul=a*b
        print("mul of a and b is :" +str(mul))
        if mul==10:
            assert True
        else:
            assert False



    def test_sub_003(self):
        a = 12
        b = 7
        sub = a - b
        print("Sub of a and b is :" + str(sub))
        if sub == 5:
            assert True
        else:
             assert False