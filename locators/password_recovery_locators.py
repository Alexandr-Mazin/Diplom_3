from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    # Кнопка восстановления пароля
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')

    # Поле ввода Email
    RECOVERY_PASSWORD = (By.CLASS_NAME, 'input__textfield')

    # Кнопка Восстановить в форме восстановления пароля
    BUTTON_RECOVERY = (By.XPATH, '//button[contains(text(),"Восстановить")]')

    # Кнопка Сохранить в форме восстановления пароля
    SAVE_RECOVERY = (By.XPATH, '//button[contains(text(),"Сохранить")]')

    # Иконка открытия пароля
    EYE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    # Активное поле ввода пароля
    ACTIVE_PASSWORD = (By.XPATH, '//div[contains(@class, "input_status_active")]')
