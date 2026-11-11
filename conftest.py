import allure
import pytest
from selenium import webdriver

from data import MAIN_PAGE
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
@allure.step("Открыть главную страницу")
def main_page(driver):
    page = MainPage(driver)
    page.open(MAIN_PAGE)
    return page


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)