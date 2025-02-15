from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


promo = "?promo=newYear"

class ProductPage(BasePage):
    def should_be_product_page(self):
        if promo != "":
            self.should_be_promo_url()
        self.should_be_add_to_basket_button()

    def should_be_promo_url(self):
        current_url = self.browser.current_url
        assert promo in current_url, "URL doesn't contain '?promo=newYear'"
        assert True

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()