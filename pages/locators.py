from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USER_NAME = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_USER_PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name=login_submit]')

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')


    #REG_USER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    #REG_USER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    #REG_USER_PASS_2 = (By.CSS_SELECTOR, '#id_registration-password2')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    TITLE_BOOK = (By.CSS_SELECTOR, 'div.alert-success strong')
    PRICE_BOOK = (By.CSS_SELECTOR, 'div.alert-info strong')
    TITLE_BOOK_1 = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    PRICE_BOOK_1 = (By.CSS_SELECTOR, 'div.col-sm-6.product_main p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')