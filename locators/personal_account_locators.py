from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    # Кнопка личный кабинет
    button_personal_account = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')

    # Кнопка Войти в аккаунт
    login_button = (By.XPATH, '//button[contains(text(),"Войти")]')

    # Поле Email на форме входа
    login_name = (By.XPATH, '//input[@name="name"]')

    # Поле Пароль в форме входа
    password_name= (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка История заказов
    history_order = (By.XPATH, '//a[contains(text(),"История заказов")]')

    # Кнопка Выход
    exit_button = (By.XPATH, '//button[contains(text(),"Выход")]')

    # Кнопка оформить заказ
    order = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
