from pages.functions_page import FunctionsPage
from pages.base_page import BasePage
from conftest import driver
import allure
from urls import Url

class TestFunctions:

    @allure.description('переход по клику на «Конструктор»')
    @allure.title('переход по клику на «Конструктор»')
    def test_click_button_constructor(self, driver):
        base_page = BasePage(driver)
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_constructor()
        assert base_page.get_url() == Url.url_constructor

    @allure.description('переход по клику на «Лента заказов»')
    @allure.title('переход по клику на «Лента заказов»')
    def test_click_order_feed(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_order_feed()
        assert function.check_displaying_title_feed_order()

    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_constructor()

        function.click_ingredient()
        assert function.check_ingredient()

    @allure.description('всплывающее окно закрывается кликом по крестику')
    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_ingredient_closed(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_constructor()

        function.click_ingredient()
        function.wait_closed()
        function.click_closed()
        assert function.check_closed

    @allure.description('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_drag_and_drop_ingredient(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_constructor()

        function.wait_bun()
        function.drag_and_drop_ingredient_to_burger_area()
        assert function.get_count_of_ingredients() == '2'

    @allure.description('залогиненный пользователь может оформить заказ')
    @allure.title('залогиненный пользователь может оформить заказ')
    def test_order_login_user(self, driver, test_user):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.login_to_account(test_user)

        function.wait_bun()
        function.drag_and_drop_ingredient_to_burger_area()
        function.click_order()
        assert function.check_order