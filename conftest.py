import pytest
from selenium import webdriver
from pages import MainPage, OrderPage
from helpers import generate_order_data


@pytest.fixture
def driver():
    """Фикстура для запуска и завершения работы браузера"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    """Фикстура для стартовой страницы"""
    page = MainPage(driver)
    page.get_main_page()
    return page


@pytest.fixture
def order_page(driver):
    """Фикстура для страницы заказа"""
    page = OrderPage(driver)
    page.get_order_page()
    return page


@pytest.fixture
def completed_order(order_page):
    """Фикстура для совершения заказа"""
    page = order_page
    order_data = generate_order_data()
    page.set_order_information(order_data)
    page.submit_order()
    return page
