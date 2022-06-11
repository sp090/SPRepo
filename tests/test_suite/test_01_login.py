import pytest
import allure

@allure.title("aaa")
class TestLogin:

    @allure.title("test a")
    @allure.description("yes a")
    def test01(self):
        print("a")
        print("b")
        print("c")

