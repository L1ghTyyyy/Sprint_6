import pytest
import allure

from helpers import generate_order_data, URLs


@allure.feature("Тестирование оформления заказа")
class TestOrder:
    """Тесты для проверки функционала оформления заказа"""

    @allure.story("Тест для кнопки «Заказать»")
    @allure.title("Тест для кнопки «Заказать» вверху страницы")
    @allure.description("На странице ищем кнопку «Заказать» вверху страницы и проверяем переход на страницу заказа")
    def test_click_on_top_order_button(self, driver, main_page):
        main_page.click_order_button_top()
        with allure.step("Проверка URL страницы заказа"):
            assert main_page.get_current_url() == URLs.ORDER_PAGE, "Переход не удался"

    @allure.story("Тест для кнопки «Заказать»")
    @allure.title("Тест для кнопки «Заказать» внизу страницы")
    @allure.description("На странице ищем кнопку «Заказать» внизу страницы и проверяем переход на страницу заказа")
    def test_click_on_bottom_order_button(self, driver, main_page):
        main_page.click_order_button_bottom()
        with allure.step("Проверка URL страницы заказа"):
            assert main_page.get_current_url() == URLs.ORDER_PAGE, "Переход не удался"

    @allure.story("Тест оформления заказа самоката")
    @allure.title("Тест успешного оформления заказа самоката")
    @allure.description("Оформляем заказ со сгенерированными данными")
    @pytest.mark.repeat(2)
    def test_order_scooter_success(self, driver, order_page):
        order_data = generate_order_data()
        order_page.set_order_information(order_data)
        order_page.submit_order()
        success_message, order_number = order_page.get_success_message()
        allure.attach(order_number, name="order_number")
        assert "Заказ оформлен" in success_message, f"Не удалось оформить заказ. Сообщение: {success_message}"

    @allure.story("Тест для лого «Самокат»")
    @allure.title("Тест для лого «Самокат» вверху страницы")
    @allure.description("На странице проверяем переход по лого Самоката на стартовую страницу")
    def test_click_on_samokat_logo(self, driver, completed_order):
        order_page = completed_order
        order_page.click_on_view_status()
        order_page.click_on_logo_samokat()
        with allure.step("Проверка URL главной страницы"):
            assert order_page.get_current_url() == URLs.BASE_URL, "Переход на главную не удался"

    @allure.story("Тест для лого «Яндекс»")
    @allure.title("Тест для лого «Яндекс» в новой вкладке")
    @allure.description("Проверка перехода по логотипу Яндекса в новой вкладке")
    def test_click_on_yandex_logo(self, driver, completed_order):
        order_page = completed_order
        order_page.click_on_view_status()
        order_page.click_on_logo_yandex()
        with allure.step("Проверка открытия страницы Дзена"):
            assert "dzen.ru" in order_page.get_current_url(), \
                f"Ожидалась страница Дзена, но была: {order_page.get_current_url()}"