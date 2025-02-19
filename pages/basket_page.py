from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket should be empty"

    def should_show_basket_is_empty_text(self):
        expected_text = "Your basket is empty. Continue shopping"
        actual_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        actual_text = actual_text.strip()

        assert (actual_text  == expected_text), \
            f"Expected text is '{expected_text}', but got '{actual_text}'"