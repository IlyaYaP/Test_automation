from .pages.product_page import ProductPage
import pytest


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

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.is_not_element_present()
