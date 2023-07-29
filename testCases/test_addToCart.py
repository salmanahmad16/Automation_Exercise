import time
import pytest
from selenium import webdriver
from pageObjects.addProductInCartPage import AddToCart
from utilities.readProperties import ReadConfig


class Test_Case_004_AddToCart:
    baseUrl = ReadConfig.getApplicationUrl()

    def test_addToCart(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.cart = AddToCart(self.driver)
        self.cart.clickProductHyperLink()
        self.cart.hoverToFirstProduct()
        self.cart.clickAddToCartFirstProduct()
        self.cart.clickContinueShopping()
        self.cart.hoverToSecondProduct()
        self.cart.clickAddToCartSecondProduct()
        self.cart.clickViewCartButton()
        time.sleep(5)
        self.driver.quit()