
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Нажать кнопку «Заказать» ({entry_point})")
    def click_order_button(self, entry_point):
        if entry_point == "top":
            self.click(MainPageLocators.ORDER_BUTTON_TOP)
        else:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
            self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть по вопросу FAQ №{index}")
    def click_faq_question(self, index):
        self.scroll_to_element(("id", f"accordion__heading-{index}"))
        self.click(("id", f"accordion__heading-{index}"))

    @allure.step("Прочитать текст ответа на вопрос №{index}")
    def get_faq_answer_text(self, index):
        answer = self.find(("id", f"accordion__panel-{index}"))
        return answer.text

    @allure.step("Кликнуть по логотипу «Самоката»")
    def click_scooter_logo(self):
        self.js_click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)