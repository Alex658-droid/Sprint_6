import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @staticmethod
    def fmt(locator, value):
        """Подставляет значение в шаблонный локатор вида ('xpath', '...{}...')."""
        return (locator[0], locator[1].format(value))

    @allure.step("Выбрать станцию метро «{station}»")
    def select_metro(self, station):
        item = self.fmt(OrderPageLocators.METRO_DROPDOWN_ITEM, station)
        for attempt in range(3):
            self.send_keys(OrderPageLocators.METRO_INPUT, station)
            try:
                self.click(item, timeout=5)
                return
            except TimeoutException:
                continue
        raise Exception(f"Не удалось выбрать станцию метро «{station}»")

    @allure.step("Заполнить форму «Для кого самокат»")
    def fill_first_form(self, data):
        self.send_keys(OrderPageLocators.FIRST_NAME, data["first_name"])
        self.send_keys(OrderPageLocators.LAST_NAME, data["last_name"])
        self.send_keys(OrderPageLocators.ADDRESS, data["address"])
        self.select_metro(data["metro"])
        self.send_keys(OrderPageLocators.PHONE, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму «Про аренду»")
    def fill_second_form(self, data):
        self.send_keys(OrderPageLocators.DATE_INPUT, data["date"])
        # Закрываем всплывший календарь, иначе он перекрывает список срока аренды
        self.press_key(OrderPageLocators.DATE_INPUT, Keys.ESCAPE)
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(self.fmt(OrderPageLocators.RENT_PERIOD_ITEM, data["period"]))
        color_id = "black" if data["color"] == "чёрный жемчуг" else "grey"
        self.click(self.fmt(OrderPageLocators.COLOR_CHECKBOX, color_id))
        self.send_keys(OrderPageLocators.COMMENT, data["comment"])
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ кнопкой «Да»")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить, что окно «Заказ оформлен» отображается")
    def is_order_success_visible(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_HEADER)

    @allure.step("Нажать «Посмотреть статус» и дождаться страницы трекинга")
    def close_success_modal(self):
        self.click(OrderPageLocators.ORDER_STATUS_BUTTON)
        self.wait_url_contains("/track")