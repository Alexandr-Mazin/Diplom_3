from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage
import allure

class PasswordRecoveryPage(BasePage):
    @allure.step('Ожидание кнопки «Восстановить пароль»')
    def wait_button_recovery_password(self):
        self.wait_visibility_element(PasswordRecoveryLocators.button_recovery_password)

    @allure.step('Клик по кнопке «Восстановить пароль»')
    def click_button_recovery_password(self):
        self.click_element(PasswordRecoveryLocators.button_recovery_password)

    @allure.step('Ожидание кнопки поля почты')
    def wait_email_recovery_password(self):
        self.wait_visibility_element(PasswordRecoveryLocators.recovery_password)

    @allure.step('Ввод почты')
    def enter_email_recovery_password(self, test_mail):
        self.enter_text(PasswordRecoveryLocators.recovery_password, test_mail)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_button_recovery(self):
        self.click_element(PasswordRecoveryLocators.button_recovery)

    @allure.step('Проверить наличие на странице кнопки сохранить')
    def wait_displaying_save(self):
        return self.wait_visibility_element(PasswordRecoveryLocators.save_recovery)

    @allure.step('Клик по иконке открытия пароля')
    def click_eye_icon(self):
        self.click_element(PasswordRecoveryLocators.eye_icon)

    @allure.step('Проверить что поле пароль активно')
    def check_active_password(self):
        return self.check_displaying_element(PasswordRecoveryLocators.active_password)



