import pytest
from selenium import webdriver


class Test_credence:
    def test_sum_001(self):
        a=3
        b=7
        sum=a+b
        print("Sum of a and b is :" +str(sum))
        if sum==10:
            assert True
        else:
            assert False

    def test_Credence_url_002(self):
        driver= webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title=="Credence":
            print("You are at crdence.in")
            assert True
        else:
            print("wrong are at site")
            assert False

    def test_sub_003(self):
        a=3
        b=7
        sub = a-b
        print("Sub of a and b is :" + str(sub))
        if sub == -4:
            assert True
        else:
            assert False


