import time
from pageObjects.basePage import BaseMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class AddToCart(BaseMethods):
    hyper_link_product = (By.CSS_SELECTOR, 'a[href="/products"]')
    button_add_to_cart_first_product = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a')
    button_add_to_cart_second_product = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div/a')
    button_view_cart = (By.CSS_SELECTOR, 'p>a[href="/view_cart"]')
    button_continue_shopping = (By.CSS_SELECTOR, '.modal-footer>button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)

    def clickProductHyperLink(self):
        self.base.click(self.hyper_link_product)

    def hoverToFirstProduct(self):
        product = self.driver.find_element(By.CSS_SELECTOR, 'img[src="/get_product_picture/1"]')
        act = ActionChains(self.driver)
        act.move_to_element(product).perform()
        time.sleep(3)

    def clickAddToCartFirstProduct(self):
        self.base.click(self.button_add_to_cart_first_product)
        time.sleep(3)

    def clickContinueShopping(self):
        self.base.click(self.button_continue_shopping)
        time.sleep(3)

    def hoverToSecondProduct(self):
        product = self.driver.find_element(By.CSS_SELECTOR, 'img[src="/get_product_picture/2"]')
        act = ActionChains(self.driver)
        act.move_to_element(product).perform()
        time.sleep(3)

    def clickAddToCartSecondProduct(self):
        self.base.click(self.button_add_to_cart_second_product)
        time.sleep(3)

    def clickViewCartButton(self):
        self.base.click(self.button_view_cart)
        time.sleep(3)



