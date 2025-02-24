from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:

    # Кнопка восстановления пароля
    button_recovery_password = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')
    # Поле ввода Email
    recovery_password = (By.CLASS_NAME, 'input__textfield')
    # Кнопка Восстановить в форме восстановления пароля
    button_recovery = (By.XPATH, '//button[contains(text(),"Восстановить")]')
    # Кнопка Сохранить в форме восстановления пароля
    save_recovery = (By.XPATH, '//button[contains(text(),"Сохранить")]')
    # Иконка открытия пароля
    eye_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    # Активное поле ввода пароля
    active_password = (By.XPATH, '//div[contains(@class, "input_status_active")]')
