from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest

def test_should_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_should_be_login_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_should_be_register_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()