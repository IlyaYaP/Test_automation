from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
import faker
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.url, 'This is not a login page'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Login form is not presented"

    def register_new_user(self, fake_email, fake_password):
        # регистрация нового пользователя
        self.go_to_login_page()
        email = self.browser.find_element(*LoginPageLocators.REG_USER_EMAIL)
        email.send_keys(fake_email)
        password = self.browser.find_element(*LoginPageLocators.REG_USER_PASS)
        password.send_keys(fake_password)
        password_2 = self.browser.find_element(*LoginPageLocators.REG_USER_PASS_2)
        password_2.send_keys(fake_password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()

