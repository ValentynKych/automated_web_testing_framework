from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest


LINKS = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
]

SINGLE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"

@pytest.mark.skip(reason="Another action")
@pytest.mark.parametrize('link', LINKS)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_book_title_in_success_popup_name()
    page.check_book_title_in_success_popup_price()

@pytest.mark.xfail(reason="Known bug, the test is expected to fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,SINGLE_LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, SINGLE_LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Known bug, the test is expected to fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, SINGLE_LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip(reason="Depends on localization requirements")
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page.should_show_basket_is_empty_text()