
class MainPageLocators:
    # Кнопки «Заказать»: верхняя в шапке, нижняя под блоком FAQ
    ORDER_BUTTON_TOP = ("xpath", "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = ("xpath", "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")

    # Аккордеон «Вопросы о важном»: вопросы и ответы пронумерованы 0–7
    FAQ_HEADING = ("id", "accordion__heading-{}")
    FAQ_PANEL = ("id", "accordion__panel-{}")

    # Логотипы в шапке
    SCOOTER_LOGO = ("xpath", "//a[contains(@class,'Header_LogoScooter')]")
    YANDEX_LOGO = ("xpath", "//a[contains(@class,'Header_LogoYandex')]")