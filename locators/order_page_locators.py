class OrderPageLocators:
    # Первая форма: «Для кого самокат»
    FIRST_NAME = ("xpath", "//input[contains(@placeholder,'Имя')]")
    LAST_NAME = ("xpath", "//input[contains(@placeholder,'Фамилия')]")
    ADDRESS = ("xpath", "//input[contains(@placeholder,'Адрес')]")
    METRO_INPUT = ("xpath", "//input[contains(@placeholder,'метро')]")
    METRO_DROPDOWN_ITEM = ("xpath", "//div[contains(@class,'select-search__select')]//button[contains(., '{}')]")
    
    PHONE = ("xpath", "//input[contains(@placeholder,'Телефон')]")
    NEXT_BUTTON = ("xpath", "//button[text()='Далее']")

    # Вторая форма: «Про аренду»
    DATE_INPUT = ("xpath", "//input[contains(@placeholder,'Когда')]")
    RENT_PERIOD_DROPDOWN = ("xpath", "//div[contains(@class,'Dropdown-control')]")
    RENT_PERIOD_ITEM = ("xpath", "//div[contains(@class,'Dropdown-option') and text()='{}']")
    COLOR_CHECKBOX = ("xpath", "//input[@id='{}']/parent::label")
    COMMENT = ("xpath", "//input[contains(@placeholder,'Комментарий')]")
    ORDER_BUTTON = ("xpath", "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON = ("xpath", "//button[text()='Да']")

    # Окно успешного заказа
    SUCCESS_HEADER = ("xpath", "//div[contains(@class,'Order_Modal')]")
    
    ORDER_STATUS_BUTTON = ("xpath", "//div[contains(@class,'Order_Modal')]//button[contains(text(),'статус')]")