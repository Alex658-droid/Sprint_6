import allure
import pytest
from data import FAQ
from pages.main_page import MainPage

# Превращаем пары (вопрос, ответ) в тройки с индексом: 0..7
FAQ_WITH_INDEX = [(i, question, answer) for i, (question, answer) in enumerate(FAQ)]


class TestFaq:
    @allure.feature("Главная страница")
    @allure.story("Вопросы о важном")
    @allure.title("Проверка выпадающего списка: вопрос №{index} открывает свой ответ")
    @pytest.mark.parametrize("index,question,expected_answer", FAQ_WITH_INDEX)
    def test_faq_answer_opens(self, main_page, index, question, expected_answer):
        with allure.step(f"Нажать на вопрос: «{question}»"):
            main_page.click_faq_question(index)
        with allure.step("Проверить, что открылся соответствующий текст ответа"):
            actual = main_page.get_faq_answer_text(index)
            assert actual == expected_answer, (
                f"Текст ответа не совпадает.\nОжидалось: {expected_answer}\nФактически: {actual}"
            )