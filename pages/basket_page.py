from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_success_basket_item(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
        "The basket is not empty"
    
    def should_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
        "The basket is not empty"