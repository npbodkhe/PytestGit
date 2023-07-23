from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Pytest:

    def test_sum_005(self):
        a = 5
        b = 4
        sum = a + b
        print(sum)
        if sum == 9:
            assert True
        else:
            assert False

    def test_sum_006(self):
        a = 10
        b = 5
        sum = a + b
        print(sum)
        if sum == 15:
            assert True
        else:
            assert False

    def test_mul_007(self):
        a = 5
        b = 10
        mul = a * b
        print(mul)
        if mul == 50:
            assert True
        else:
            assert False

    def test_credence_URL_008(self):
        driver = webdriver.Firefox()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("LogIn Successful")
        else:
            print("LogIn Failed")