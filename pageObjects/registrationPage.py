import time

from pageObjects.basePage import BaseMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class RegistrationPage(BaseMethods):
    hyper_link_signup = (By.LINK_TEXT, 'Signup / Login')
    text_username_selector = (By.CSS_SELECTOR, 'input[name="name"]')
    text_email_selector = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    button_signup_selector = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
    text_new_user_signup = (By.CSS_SELECTOR, '.signup-form>h2')
    text_enter_account_information = (By.CSS_SELECTOR, '.login-form>h2')
    radio_select_gender_mr = (By.CSS_SELECTOR, f"label[for='id_gender1']")
    input_name = (By.CSS_SELECTOR, 'input[id="name"]')
    input_email = (By.CSS_SELECTOR, 'input[id="email"]')
    input_password = (By.CSS_SELECTOR, 'input[id="password"]')
    set_date = 'select[id="days"]'
    set_month = 'select[id="months"]'
    set_year = 'select[id="years"]'
    checkmark_newsletter = (By.CSS_SELECTOR, 'input[id="newsletter"]')
    checkmark_specialOffers = (By.CSS_SELECTOR, 'input[id="optin"]')
    input_first_name = (By.CSS_SELECTOR, 'input[id="first_name"]')
    input_last_name = (By.CSS_SELECTOR, 'input[id="last_name"]')
    input_company = (By.CSS_SELECTOR, 'input[id="company"]')
    input_address = (By.CSS_SELECTOR, 'input[id="address1"]')
    set_country = 'select[id="country"]'
    input_state = (By.CSS_SELECTOR, 'input[id="state"]')
    input_city = (By.CSS_SELECTOR, 'input[id="city"]')
    input_zipCode = (By.CSS_SELECTOR, 'input[id="zipcode"]')
    input_mobileNumber = (By.CSS_SELECTOR, 'input[id="mobile_number"]')
    button_create_account = (By.CSS_SELECTOR, 'button[data-qa="create-account"]')
    text_account_created = (By.CSS_SELECTOR, 'h2>b')
    button_continue = (By.CSS_SELECTOR, 'a[data-qa="continue-button"]')
    text_account_holder_name = (By.CSS_SELECTOR, 'li>a>b')
    hyper_link_delete_account = (By.LINK_TEXT, 'Delete Account')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)

    def clickSignupHyperLink(self):
        self.base.click(self.hyper_link_signup)

    def enterUserName(self, username):
        self.base.send_values(self.text_username_selector, username)

    def enterSignupEmail(self, signup_email):
        self.base.send_values(self.text_email_selector, signup_email)

    def clickSignupButton(self):
        self.base.click(self.button_signup_selector)

    def getNewUserSignupText(self):
        text = self.base.get_text(self.text_new_user_signup)
        return text

    def getEnterAccountInformationText(self):
        text = self.base.get_text(self.text_enter_account_information)
        return text

    def selectGender(self):
        self.base.click(self.radio_select_gender_mr)

    def enterNewUserName(self, username):
        self.base.send_values(self.input_name, username)

    def enterNewUserEmail(self, email):
        self.base.send_values(self.input_email, email)

    def enterNewUserPassword(self, password):
        self.base.send_values(self.input_password, password)

    def selectDOB(self):
        drop_date = Select(self.driver.find_element(By.CSS_SELECTOR, self.set_date))
        time.sleep(1)
        drop_date.select_by_visible_text("16")

        drop_month = Select(self.driver.find_element(By.CSS_SELECTOR, self.set_month))
        time.sleep(1)
        drop_month.select_by_visible_text("August")

        drop_year = Select(self.driver.find_element(By.CSS_SELECTOR, self.set_year))
        time.sleep(1)
        drop_year.select_by_visible_text("1996")

    def checkNewsLetter(self):
        self.base.click(self.checkmark_newsletter)

    def checkSpecialOffers(self):
        self.base.click(self.checkmark_specialOffers)

    # Additional Address
    def enterFirstName(self, name):
        self.base.send_values(self.input_first_name, name)

    def enterLastName(self, name):
        self.base.send_values(self.input_last_name, name)

    def enterCompany(self, name):
        self.base.send_values(self.input_company, name)

    def enterAddress(self, address):
        self.base.send_values(self.input_address, address)

    def selectCountry(self):
        drop_country = Select(self.driver.find_element(By.CSS_SELECTOR, self.set_country))
        time.sleep(2)
        drop_country.select_by_visible_text("Canada")
    
    def enterState(self, state):
        self.base.send_values(self.input_state, state)
    
    def enterCity(self, city):
        self.base.send_values(self.input_city, city)
    
    def enterZipCode(self, zipcode):
        self.base.send_values(self.input_zipCode, zipcode)

    def enterMobileNumber(self, mobile):
        self.base.send_values(self.input_mobileNumber, mobile)

    def clickOnCreateAccountButton(self):
        self.base.click(self.button_create_account)
        time.sleep(3)

    def getAccountStatus(self):
        text = self.base.get_text(self.text_account_created)
        return text

    def clickContinueButton(self):
        self.base.click(self.button_continue)

    def getAccountHolderName(self):
        text = self.base.get_text(self.text_account_holder_name)
        return text

    def clickOnDeleteAccount(self):
        self.base.click(self.hyper_link_delete_account)





