import allure
from urllib.parse import urlparse
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по адресу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Дождаться появления элемента: {locator}")
    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step("Клик по элементу через JavaScript: {locator}")
    def js_click(self, locator, timeout=10):
        element = self.find(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def send_keys(self, locator, text, timeout=10):
        element = self.find(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Нажать клавишу в поле: {locator}")
    def press_key(self, locator, key, timeout=10):
        self.find(locator, timeout).send_keys(key)

    @allure.step("Проверить, что элемент видим: {locator}")
    def is_element_displayed(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Дождаться, пока браузер окажется ровно на '{url}'")
    def wait_url_to_be(self, url, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    @allure.step("Дождаться, пока URL будет содержать '{text}'")
    def wait_url_contains(self, text, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(text)
        )

    @allure.step("Дождаться перехода на домен '{domain}'")
    def wait_for_domain(self, domain, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda drv: urlparse(drv.current_url).netloc.endswith(domain)
        )

    @allure.step("Проскроллить к элементу: {locator}")
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получить текущий адрес страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новое окно браузера")
    def switch_to_new_window(self):
        current = self.driver.current_window_handle
        new_handle = [h for h in self.driver.window_handles if h != current][0]
        self.driver.switch_to.window(new_handle)