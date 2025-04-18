import allure
import random
from locators.order_page_locators import (
    NAME_INPUT_LOCATOR,
    SURNAME_INPUT_LOCATOR,
    ADDRESS_INPUT_LOCATOR,
    METRO_FIELD_LOCATOR,
    METRO_OPTIONS_LOCATOR,
    PHONE_INPUT_LOCATOR,
    NEXT_BUTTON_LOCATOR,
    DELIVERY_DATE_LOCATOR,
    RENTAL_PERIOD_LOCATOR,
    RENTAL_OPTIONS_LOCATOR,
    COLOR_LOCATOR,
    COMMENT_INPUT_LOCATOR,
    ORDER_BUTTON_LOCATOR,
    CONFIRM_BUTTON_LOCATOR,
    SUCCESS_MESSAGE_LOCATOR,
    VIEW_STATUS_BUTTON_LOCATOR,
    LOOK_BUTTON_LOCATOR,
    LOGO_SCOOTER,
    LOGO_YANDEX,
    get_date_locator,
)
from helpers import URLs
from .base_page import BasePage


class OrderPage(BasePage):
    """Page Object для страницы заказа самоката"""

    @allure.step("Открыть страницу заказа")
    def get_order_page(self):
        self.get_page(URLs.ORDER_PAGE)

    @allure.step("Заполнение первой страницы формы заказа")
    def fill_first_order_form(self, name: str, surname: str, address: str, phone: str):
        self.send_keys(NAME_INPUT_LOCATOR, name)
        self.send_keys(SURNAME_INPUT_LOCATOR, surname)
        self.send_keys(ADDRESS_INPUT_LOCATOR, address)
        self.select_random_metro_station()
        self.send_keys(PHONE_INPUT_LOCATOR, phone)

    @allure.step("Случайный выбор станции метро")
    def select_random_metro_station(self):
        self.click_on(METRO_FIELD_LOCATOR)
        self.wait_for_element_to_be_visible(METRO_OPTIONS_LOCATOR)
        options = self.find_elements(METRO_OPTIONS_LOCATOR)
        station = random.choice(options)
        self.scroll_to_element(station)
        station.click()

    @allure.step("Перейти к следующему шагу заказа")
    def click_next_page(self):
        self.click_on(NEXT_BUTTON_LOCATOR)

    @allure.step("Заполнение второй страницы формы заказа")
    def fill_second_order_form(self, delivery_date: str, comment: str):
        self.set_delivery_date(delivery_date)
        self.select_rental_period()
        self.select_scooter_color()
        self.send_keys(COMMENT_INPUT_LOCATOR, comment)

    @allure.step("Установка даты доставки: {delivery_date}")
    def set_delivery_date(self, delivery_date: str):
        self.click_on(DELIVERY_DATE_LOCATOR)
        self.send_keys(DELIVERY_DATE_LOCATOR, delivery_date)
        locator = get_date_locator(int(delivery_date.split('.')[0]))
        self.click_on(locator)

    @allure.step("Случайный выбор срока аренды")
    def select_rental_period(self):
        self.click_on(RENTAL_PERIOD_LOCATOR)
        options = self.find_elements(RENTAL_OPTIONS_LOCATOR)
        period = random.choice(options)
        self.scroll_to_element(period)
        period.click()

    @allure.step("Случайный выбор цвета самоката")
    def select_scooter_color(self):
        colors = self.find_elements(COLOR_LOCATOR)
        random.choice(colors).click()

    @allure.step("Заполнить всю форму заказа")
    def set_order_information(self, order_data: dict):
        name = order_data.get('name', '')
        surname = order_data.get('surname', '')
        address = order_data.get('address', '')
        phone = order_data.get('phone', '')
        delivery_date = order_data.get('delivery_date', '')
        comment = order_data.get('comment', '')
        self.fill_first_order_form(name, surname, address, phone)
        self.click_next_page()
        self.fill_second_order_form(delivery_date, comment)

    @allure.step("Подтверждение заказа")
    def submit_order(self):
        self.click_on(ORDER_BUTTON_LOCATOR)
        self.click_on(CONFIRM_BUTTON_LOCATOR)

    @allure.step("Получение сообщения об успешном заказе")
    def get_success_message(self) -> tuple[str, str]:
        text = self.find_element(SUCCESS_MESSAGE_LOCATOR).text
        number = text.split(":")[1].split(".")[0].strip()
        return text, number

    @allure.step("Просмотр статуса заказа")
    def click_on_view_status(self):
        self.click_on(VIEW_STATUS_BUTTON_LOCATOR)
        self.wait_for_element_to_be_visible(LOOK_BUTTON_LOCATOR)

    @allure.step("Клик по логотипу Самоката и возврат на главную")
    def click_on_logo_samokat(self):
        self.click_on(LOGO_SCOOTER)
        self.wait_for_page(URLs.BASE_URL)

    @allure.step("Клик по логотипу Яндекса и открытие Дзена")
    def click_on_logo_yandex(self):
        self.click_on(LOGO_YANDEX)
        self.switch_to_new_window_with_url_contains("dzen.ru")