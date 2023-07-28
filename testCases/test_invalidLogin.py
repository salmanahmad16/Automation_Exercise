import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import InvalidLoginPage


class Test_Case_003_InvalidLogin:
    baseUrl = 'http://automationexercise.com'
    name = "abc"
    email_address = "salman@leo788888.com"
    password = "1234dadadad56"

    def test_InvalidLogin(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.invalid_login = InvalidLoginPage(self.driver)
        self.invalid_login.clickSigninHyperLink()
        time.sleep(2)
        assert "Login to your account" in self.invalid_login.getLoginIntoAccountText()
        self.invalid_login.enterInvalidLoginEmail(self.email_address)
        self.invalid_login.enterInvalidLoginPassword(self.password)
        self.invalid_login.clickLoginButton()
        time.sleep(2)
        if self.invalid_login.getErrorMessageText() == "Your email or password is incorrect":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_InvalidLogin.png")
        time.sleep(5)
        self.driver.quit()


