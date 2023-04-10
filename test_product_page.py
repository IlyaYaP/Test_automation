from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time
import faker


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

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(3)
#     page.guest_can_add_product_to_basket()
#     time.sleep(3)
#     page.should_not_be_success_message()


# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(5)
#     page.should_not_be_success_message()

# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_can_add_product_to_basket()
#     page.should_not_be_success_message_dis()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_basket_page()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_not_be_success_basket_item()
#     basket_page.should_basket_empty_message()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        fake_email = f.email()
        fake_password = f.password()

        self.link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = LoginPage(browser, self.link)
        page.open()
        page.register_new_user(fake_email, fake_password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.guest_can_add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()


