
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @staticmethod
    def fmt(locator, value):
        """Подставляет значение в шаблонный локатор вида ('xpath', '...{}...')."""
        return (locator[0], locator[1].format(value))

    def select_metro(self, station):
        item = self.fmt(OrderPageLocators.METRO_DROPDOWN_ITEM, station)
        for attempt in range(3):
            input_field = self.find(OrderPageLocators.METRO_INPUT)
            input_field.send_keys(Keys.CONTROL, "a")
            input_field.send_keys(station)
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(item)
                ).click()
            except TimeoutException:
                continue
            if station in self.find(OrderPageLocators.METRO_INPUT).get_attribute("value"):
                return
        raise Exception(f"Не удалось выбрать станцию метро «{station}»")

    def fill_first_form(self, data):
        self.send_keys(OrderPageLocators.FIRST_NAME, data["first_name"])
        self.send_keys(OrderPageLocators.LAST_NAME, data["last_name"])
        self.send_keys(OrderPageLocators.ADDRESS, data["address"])
        self.select_metro(data["metro"])
        self.send_keys(OrderPageLocators.PHONE, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, data):
        self.click(OrderPageLocators.DATE_INPUT)
        self.driver.switch_to.active_element.send_keys(data["date"])
        # Закрываем всплывший календарь, иначе он перекрывает список срока аренды
        self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(self.fmt(OrderPageLocators.RENT_PERIOD_ITEM, data["period"]))
        color_id = "black" if data["color"] == "чёрный жемчуг" else "grey"
        self.click(self.fmt(OrderPageLocators.COLOR_CHECKBOX, color_id))
        self.send_keys(OrderPageLocators.COMMENT, data["comment"])
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    def is_order_success_visible(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_HEADER)

    def close_success_modal(self):
        self.click(OrderPageLocators.ORDER_STATUS_BUTTON)
        self.wait_url_contains("/track")