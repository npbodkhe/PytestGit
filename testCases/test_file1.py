from selenium import webdriver
from selenium.webdriver.common.service import Service
headless_option = webdriver.ChromeOptions()
headless_option.add_argument("headless")


class Test_Pytest:

    def test_sum_001(self):
        a = 5
        b = 54
        sum = a + b
        print(sum)
        if sum == 59:
            assert True
        else:
            assert False

    def test_sum_002(self):
        a = 50
        b = 5
        sum = a + b
        print(sum)
        if sum == 55:
            assert True
        else:
            assert False

    def test_mul_003(self):
        a = 5
        b = 4
        mul = a * b
        print(mul)
        if mul == 20:
            assert True
        else:
            assert False

    def test_credence_URL_004(self):

        driver = webdriver.Chrome(options = headless_option)
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("LogIn Successful")
        else:
            print("LogIn Failed")