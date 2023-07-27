import time
import pytest
from selenium import webdriver
from pageObjects.registrationPage import RegistrationPage


class Test_Case_001_Registration:
    baseUrl = 'http://automationexercise.com'
    name = "salman"
    email_address = "salman@leo.com"

    def test_registration(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.regPage = RegistrationPage(self.driver)
        self.regPage.clickSignupHyperLink()
        time.sleep(2)
        assert "New User Signup!" in self.regPage.getNewUserSignupText()  # Check new user signup is visible on page
        self.regPage.enterUserName(self.name)
        self.regPage.enterSignupEmail(self.email_address)
        self.regPage.clickSignupButton()
        time.sleep(2)
        assert "ENTER ACCOUNT INFORMATION" in self.regPage.getEnterAccountInformationText()
        self.regPage.selectGender()
        self.regPage.enterNewUserName("Lion")
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
        assert "ACCOUNT CREATED!" in self.regPage.getAccountStatus()
        self.regPage.clickContinueButton()
        time.sleep(3)
        assert "Lion" in self.regPage.getAccountHolderName()
        self.regPage.clickOnDeleteAccount()
        time.sleep(2)
        assert "ACCOUNT DELETED!" in self.regPage.getAccountStatus()
        time.sleep(2)
        self.regPage.clickContinueButton()




