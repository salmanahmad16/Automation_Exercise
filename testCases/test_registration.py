import time
import pytest
from selenium import webdriver
from pageObjects.registrationPage import RegistrationPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger


class Test_Case_001_Registration:
    baseUrl = ReadConfig.getApplicationUrl()
    logger = CustomLogger("/Users/mac/PycharmProjects/automationExercise/Logs/automation.log").logger
    name = "salman6"
    email_address = "salman@leo8.com"

    def test_registration(self, setup):
        self.logger.info("********* Test Case 001 User Registration ******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.regPage = RegistrationPage(self.driver)
        self.regPage.clickSignupHyperLink()
        time.sleep(2)
        self.logger.debug("********* Verify Signup button is visible ******")
        assert "New User Signup!" in self.regPage.getNewUserSignupText()  # Check new user signup is visible on page
        self.regPage.enterUserName(self.name)
        self.regPage.enterSignupEmail(self.email_address)
        self.regPage.clickSignupButton()
        time.sleep(2)

        assert "ENTER ACCOUNT INFORMATION" in self.regPage.getEnterAccountInformationText()
        self.regPage.selectGender()
        self.regPage.enterNewUserName("Lion8")
        self.regPage.enterNewUserPassword("123456")
        self.regPage.selectDOB()
        self.regPage.checkNewsLetter()
        self.regPage.checkSpecialOffers()
        self.regPage.enterFirstName("salman")
        self.regPage.enterLastName("ahmad")
        self.regPage.enterCompany("MyCompany")
        self.regPage.enterAddress("Thokar")
        self.regPage.selectCountry()
        self.regPage.enterState("Haryana")
        self.regPage.enterCity("Sahiwal")
        self.regPage.enterZipCode("00000")
        self.regPage.enterMobileNumber("03317789065")
        self.regPage.clickOnCreateAccountButton()
        self.logger.info("********* Account Created ******")
        assert "ACCOUNT CREATED!" in self.regPage.getAccountStatus()
        self.regPage.clickContinueButton()
        time.sleep(3)
        self.logger.info("********* Verify account name ******")
        assert "Lion" in self.regPage.getAccountHolderName()
        self.regPage.clickOnDeleteAccount()
        time.sleep(2)
        self.logger.info("********* Account Deleted ******")
        assert "ACCOUNT DELETED!" in self.regPage.getAccountStatus()
        time.sleep(2)
        self.regPage.clickContinueButton()




