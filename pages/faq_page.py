import allure
from helpers import URLs
from locators.faq_page_locators import question_locator, answer_locator
from .base_page import BasePage


class FAQPage(BasePage):
    """Класс Page Object для раздела FAQ"""

    @allure.step("Открыть страницу FAQ")
    def get_faq_page(self):
        """Открывает раздел «Вопросы о важном»"""
        self.get_page(URLs.BASE_URL + "#faq")

    @allure.step("Клик по вопросу: {question_text}")
    def click_on_question(self, question_text: str):
        locator = question_locator(question_text)
        self.scroll_to(locator)
        self.click_on(locator)

    @allure.step("Получение текста и видимости ответа для вопроса: {question_text}")
    def get_answer_text(self, question_text: str) -> tuple[str, bool]:
        locator = answer_locator(question_text)
        answer_elem = self.wait_for_element_to_be_visible(locator)
        return answer_elem.text, answer_elem.is_displayed()