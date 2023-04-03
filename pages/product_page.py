from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_not_be_success_message_dis(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_title_and_price(self):
        title_book = self.browser.find_element(*ProductPageLocators.TITLE_BOOK).text
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        title_book_1 = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_1).text
        price_book_1 = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_1).text

        assert title_book == title_book_1, 'NO OK TITLE'
        assert price_book == price_book_1, 'NO OK PRICE'