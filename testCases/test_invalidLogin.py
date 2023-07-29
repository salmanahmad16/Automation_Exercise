import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import InvalidLoginPage
import allure
from allure_commons.types import AttachmentType

from utilities.customLogger import CustomLogger


@allure.severity(allure.severity_level.NORMAL)
class Test_Case_003_InvalidLogin:
    baseUrl = 'http://automationexercise.com'
    name = "abc"
    email_address = "salman@leo788888.com"
    password = "1234dadadad56"
    logger = CustomLogger("/Users/mac/PycharmProjects/automationExercise/Logs/automation.log").logger

    @allure.severity(allure.severity_level.CRITICAL)
    def test_InvalidLogin(self, setup):
        self.logger.info("********* Test Case 000 Invalid User ******")
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
            self.logger.info("********* Test Pass ******")
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="invalid_login", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("./Screenshots/" + "test_InvalidLogin.png")
            self.logger.info("********* Test Fail ******")


        time.sleep(2)
        self.driver.quit()
