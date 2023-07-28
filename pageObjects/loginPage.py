import time
from pageObjects.basePage import BaseMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class LoginPage(BaseMethods):
    hyper_link_signin = (By.LINK_TEXT, 'Signup / Login')
    text_login_account_text = (By.CSS_SELECTOR, 'div.login-form>h2')
    input_login_email = (By.CSS_SELECTOR, 'form[action="/login"] input[name="email"]')
    input_login_password = (By.CSS_SELECTOR, 'form[action="/login"] input[name="password"]')
    button_login = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
    hyper_link_delete_account = (By.LINK_TEXT, 'Delete Account')
    text_account_holder_name = (By.CSS_SELECTOR, 'li>a>b')
    text_account_status = (By.CSS_SELECTOR, 'h2>b')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)

    def clickSigninHyperLink(self):
        self.base.click(self.hyper_link_signin)

    def getLoginIntoAccountText(self):
        text = self.base.get_text(self.text_login_account_text)
        return text

    def enterValidLoginEmail(self, email):
        self.base.send_values(self.input_login_email, email)

    def enterValidLoginPassword(self, password):
        self.base.send_values(self.input_login_password, password)

    def clickLoginButton(self):
        self.base.click(self.button_login)

    def getAccountHolderName(self):
        text = self.base.get_text(self.text_account_holder_name)
        return text

    def clickOnDeleteAccount(self):
        self.base.click(self.hyper_link_delete_account)

    def getAccountStatus(self):
        text = self.base.get_text(self.text_account_status)
        return text


class InvalidLoginPage(BaseMethods):
    hyper_link_signin = (By.LINK_TEXT, 'Signup / Login')
    text_login_account_text = (By.CSS_SELECTOR, 'div.login-form>h2')
    input_login_email = (By.CSS_SELECTOR, 'form[action="/login"] input[name="email"]')
    input_login_password = (By.CSS_SELECTOR, 'form[action="/login"] input[name="password"]')
    button_login = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
    text_error_message = (By.CSS_SELECTOR, 'form[action="/login"]>p')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)

    def clickSigninHyperLink(self):
        self.base.click(self.hyper_link_signin)

    def getLoginIntoAccountText(self):
        text = self.base.get_text(self.text_login_account_text)
        return text

    def enterInvalidLoginEmail(self, email):
        self.base.send_values(self.input_login_email, email)

    def enterInvalidLoginPassword(self, password):
        self.base.send_values(self.input_login_password, password)

    def clickLoginButton(self):
        self.base.click(self.button_login)

    def getErrorMessageText(self):
        text = self.base.get_text(self.text_error_message)
        return text
