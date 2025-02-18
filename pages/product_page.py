from .base_page import BasePage
from .locators import ProductPageLocators


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

    def check_book_title_in_success_popup_name(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_ALERT).text == self.browser.find_element(
            *ProductPageLocators.NAME_OF_PRODUCT).text, "Names of item are different"

    def check_book_title_in_success_popup_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text == self.browser.find_element(
            *ProductPageLocators.PRICE_OF_PRODUCT_ALERT).text, "Prices of item are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

