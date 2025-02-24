from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage
import allure

class AccountPage(BasePage):

    @allure.step('Вход в ЛК')
    def login_to_account(self, test_user):
        email = test_user["email"]
        password = test_user["password"]
        self.enter_text(PersonalAccountLocators.login_name, email)
        self.enter_text(PersonalAccountLocators.password_name, password)
        self.click_element(PersonalAccountLocators.login_button)


    @allure.step('Ожидание кнопки «Войти»')
    def wait_button_account(self):
        self.wait_clickable_element(PersonalAccountLocators.login_button)

    @allure.step('Клик по кнопке «Войти»')
    def click_button_account(self):
        self.click_element(PersonalAccountLocators.login_button)

    @allure.step('Ожидание кнопки «Личный кабинет»')
    def wait_button_personal_account(self):
        self.wait_clickable_element(PersonalAccountLocators.button_personal_account)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_button_personal_account(self):
        self.click_element(PersonalAccountLocators.button_personal_account)

    @allure.step('Ожидание кнопки «История заказов»')
    def wait_history_order(self):
        self.wait_clickable_element(PersonalAccountLocators.history_order)

    @allure.step('Клик кнопки «История заказов»')
    def click_history_order(self):
        self.click_element(PersonalAccountLocators.history_order)

    @allure.step('Клик кнопки «Выход»')
    def click_exit(self):
        self.click_element(PersonalAccountLocators.exit_button)

