from .pages.product_page import ProductPage
import pytest
import time


# @pytest.mark.parametrize('link', [6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   9])
# def test_guest_can_add_product_to_basket(browser, link):
#     link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_can_add_product_to_basket()


# @pytest.mark.parametrize('link', [6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   9])
# def test_should_be_title_and_price(browser, link):
#     pytest.param(link, marks=pytest.mark.xfail)
#     link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_can_add_product_to_basket()
#     page.should_be_title_and_price()
#     page.should_not_be_success_message()
#     page.should_not_be_success_message_dis()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    time.sleep(3)
    page.guest_can_add_product_to_basket()
    time.sleep(3)
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.should_not_be_success_message_dis()
