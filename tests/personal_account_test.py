from pages.personal_account_page import AccountPage
from pages.base_page import BasePage
from conftest import driver
import allure
from urls import Url

class TestPersonalAccount:

    @allure.description('Переход по клику на «Личный кабинет»')
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_personal_account(self, driver, test_user):
        base_page = BasePage(driver)
        account_page = AccountPage(driver)

        account_page.wait_button_account()
        account_page.login_to_account(test_user)

        account_page.wait_button_personal_account()
        account_page.click_button_personal_account()

        account_page.wait_history_order()

        assert base_page.get_url() == Url.url_personal_account

    @allure.description('Переход в раздел «История заказов»')
    @allure.title('Переход в раздел «История заказов»')
    def test_history_order(self, driver, test_user):
        base_page = BasePage(driver)
        account_page = AccountPage(driver)

        account_page.wait_button_account()
        account_page.login_to_account(test_user)

        account_page.wait_button_personal_account()
        account_page.click_button_personal_account()

        account_page.wait_history_order()
        account_page.click_history_order()

        assert base_page.get_url() == Url.url_history_order

    @allure.description('выход из аккаунта')
    @allure.title('Выход из аккаунта')
    def test_exit_order(self, driver, test_user):
        account_page = AccountPage(driver)

        account_page.wait_button_account()
        account_page.login_to_account(test_user)

        account_page.wait_button_personal_account()
        account_page.click_button_personal_account()

        account_page.wait_history_order()
        account_page.click_exit()

        assert account_page.wait_button_account