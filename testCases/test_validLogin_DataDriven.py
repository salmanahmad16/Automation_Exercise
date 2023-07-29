import logging
import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.customLogger import CustomLogger
from utilities import ExcelUtils


class Test_Case_0002_Login_DataDriven:
    baseUrl = 'http://automationexercise.com'
    name = "Lion6"
    path = './TestData/logins.xlsx'
    logger = CustomLogger("/Users/mac/PycharmProjects/automationExercise/Logs/automation.log").logger

    def test_Login(self, setup):
        self.logger.info("********* Test Case 000 Data Driven Test For Valid User ******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.clickSigninHyperLink()
        time.sleep(2)

        self.row = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Rows in file , ", self.row)
        list_status = []
        for r in range(2, self.row+1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
            self.login.enterValidLoginEmail(self.user)
            self.login.enterValidLoginPassword(self.password)
            self.login.clickLoginButton()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Automation Exercise"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("Test Is Pass")
                    self.login.clickOnLogoutButton()
                    list_status.append("Pass")
                    time.sleep(2)
            elif act_title != exp_title:
                if self.exp == "fail":
                    self.logger.info("Test Is Pass")
                    list_status.append("pass")


