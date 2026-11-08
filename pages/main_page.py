from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_order_button(self, entry_point):
        if entry_point == "top":
            self.click(MainPageLocators.ORDER_BUTTON_TOP)
        else:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
            self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_faq_question(self, index):
        self.scroll_to_element(("id", f"accordion__heading-{index}"))
        self.click(("id", f"accordion__heading-{index}"))

    def get_faq_answer_text(self, index):
        answer = self.find(("id", f"accordion__panel-{index}"))
        return answer.text

    def click_scooter_logo(self):
        element = self.find(MainPageLocators.SCOOTER_LOGO)
        self.driver.execute_script("arguments[0].click();", element)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def switch_to_new_window(self):
        new_handle = [h for h in self.driver.window_handles if h != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_handle)