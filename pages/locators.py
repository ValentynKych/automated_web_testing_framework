from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
     REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main p")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_PRODUCT_ALERT = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_OF_PRODUCT_ALERT = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE =(By.CSS_SELECTOR, ".content #content_inner")