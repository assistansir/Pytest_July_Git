class Test_credence_001:
    def test_mul_004(self):
        a=5
        b=4
        mul=a*b
        print("mul of a and b is :" +str(mul))
        if mul==20:
            assert True
        else:
            assert False