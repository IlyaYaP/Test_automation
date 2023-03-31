from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USER_NAME = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_USER_PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name=login_submit]')

    REG_USER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_USER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_USER_PASS_2 = (By.CSS_SELECTOR, '#id_registration-password2')