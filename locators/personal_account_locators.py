from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    # Кнопка личный кабинет
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')

    # Кнопка Войти в аккаунт
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')

    # Поле Email на форме входа
    LOGIN_NAME = (By.XPATH, '//input[@name="name"]')

    # Поле Пароль в форме входа
    PASSWORD_NAME = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка История заказов
    HISTORY_ORDER = (By.XPATH, '//a[contains(text(),"История заказов")]')

    # Кнопка Выход
    EXIT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]')

    # Кнопка оформить заказ
    ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
