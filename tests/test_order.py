import allure
from urllib.parse import urlparse

import pytest
from data import MAIN_PAGE, ORDER_DATA, ENTRY_POINTS
from pages.order_page import OrderPage


class TestOrder:
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий")
    @allure.title("Заказ оформлен: точка входа «{entry_point}», данные «{data[first_name]} {data[last_name]}»")
    @pytest.mark.parametrize("entry_point", ENTRY_POINTS)
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_positive_flow(self, main_page, order_page, entry_point, data):
        with allure.step(f"Нажать кнопку «Заказать» ({entry_point})"):
            main_page.click_order_button(entry_point)
        with allure.step("Заполнить первую форму заказа"):
            order_page.fill_first_form(data)
        with allure.step("Заполнить вторую форму заказа"):
            order_page.fill_second_form(data)
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        with allure.step("Проверить появление окна «Заказ оформлен»"):
            assert order_page.is_order_success_visible(), "Окно об успешном заказе не появилось"
        with allure.step("Закрыть окно кнопкой «Посмотреть статус»"):
            order_page.close_success_modal()
        with allure.step("Клик по логотипу «Самоката» ведёт на главную страницу"):
            main_page.click_scooter_logo()
            main_page.wait_url_to_be(MAIN_PAGE)
            assert main_page.get_current_url() == MAIN_PAGE, (
                f"Логотип «Самоката» не ведёт на главную: {main_page.get_current_url()}"
            )


class TestLogoRedirect:
    @allure.feature("Заказ самоката")
    @allure.story("Редиректы логотипов")
    @allure.title("Клик по логотипу Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen(self, main_page):
        with allure.step("Кликнуть по логотипу Яндекса"):
            main_page.click_yandex_logo()
        with allure.step("Переключиться в новое окно и проверить редирект на Дзен"):
            main_page.switch_to_new_window()
            main_page.wait_for_domain("dzen.ru")
            assert urlparse(main_page.get_current_url()).netloc == "dzen.ru", (
                f"Редирект на Дзен не сработал: {main_page.get_current_url()}"
            )