import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage


class Test_Case_002_ValidLogin:
    baseUrl = 'http://automationexercise.com'
    name = "Lion6"
    email_address = "salman@leo7.com"
    password = "123456"

    def test_validLogin(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.clickSigninHyperLink()
        time.sleep(2)
        assert "Login to your account" in self.login.getLoginIntoAccountText()
        self.login.enterValidLoginEmail(self.email_address)
        self.login.enterValidLoginPassword(self.password)
        self.login.clickLoginButton()
        time.sleep(2)
        assert "Lion6" in self.login.getAccountHolderName()
        self.login.clickOnDeleteAccount()
        time.sleep(2)
        assert "ACCOUNT DELETED!" in self.login.getAccountStatus()
        time.sleep(2)

