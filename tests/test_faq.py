import pytest
import allure

from pages.faq_page import FAQPage
from data.faq_data import QUESTIONS_AND_ANSWERS


@allure.feature("Тестирование раздела FAQ")
class TestFAQPage:
    """Тесты для раздела «Вопросы о важном»"""

    @pytest.mark.parametrize("item", QUESTIONS_AND_ANSWERS)
    @allure.story("Проверка вопросов и ответов в разделе FAQ")
    @allure.title("Тест для вопроса: {item[question]}")
    @allure.description("На странице ищем вопрос и проверяем, что ответ ему соответствует")
    def test_faq_click_on_questions(self, driver, item):
        faq_page = FAQPage(driver)
        faq_page.get_faq_page()
        faq_page.click_on_question(item["question"])
        answer_text, is_visible = faq_page.get_answer_text(item["question"])

        assert is_visible, "Ответ должен отображаться"
        assert answer_text == item["expected"], (
            f"Ожидался ответ '{item['expected']}', но получили '{answer_text}'"
        )