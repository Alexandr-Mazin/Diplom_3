from locators.functions_locators import FunctionsLocators
from pages.base_page import BasePage
import allure

class FunctionsPage(BasePage):
    @allure.step('Ожидание кнопки «Конструктор»')
    def wait_button_constructor(self):
        self.wait_visibility_element(FunctionsLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по кнопке «Конструктор»')
    def click_button_constructor(self):
        self.click_element(FunctionsLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_button_order_feed(self):
        self.click_element(FunctionsLocators.BUTTON_FEED)

    @allure.step('Проверить наличие на странице заголовка Лента заказов')
    def check_displaying_title_feed_order(self):
        return self.check_displaying_element(FunctionsLocators.TITLE_FEED_ORDER)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_element(FunctionsLocators.INGREDIENT_BUN)

    @allure.step('Проверить открытие карточки ингредиента')
    def check_ingredient(self):
        return self.check_displaying_element(FunctionsLocators.INGREDIENT_BUN_INFO)

    @allure.step('Клик по крестику')
    def click_closed(self):
        self.click_element(FunctionsLocators.INGREDIENT_CLOSED)

    @allure.step('Ожидание крестика')
    def wait_closed(self):
        self.wait_clickable_element(FunctionsLocators.INGREDIENT_CLOSED)

    @allure.step('Проверить отсутствие крестика')
    def check_closed(self):
        return not self.check_displaying_element(FunctionsLocators.INGREDIENT_CLOSED)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_burger_area(self):
        source_element = self.driver.find_element(*FunctionsLocators.INGREDIENT_BUN)
        target_element = self.driver.find_element(*FunctionsLocators.BURGER_AREA)

        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_element(FunctionsLocators.COUNT_INGREDIENT)

    @allure.step('Ожидание булочки')
    def wait_bun(self):
        self.wait_clickable_element(FunctionsLocators.BURGER_AREA)

    @allure.step('Вход в ЛК')
    def login_to_account(self, test_user):
        email = test_user["email"]
        password = test_user["password"]
        self.enter_text(FunctionsLocators.LOGIN_NAME, email)
        self.enter_text(FunctionsLocators.PASSWORD_NAME, password)
        self.click_element(FunctionsLocators.LOGIN_BUTTON)

    @allure.step('Клик по Оформить заказ')
    def click_order(self):
        self.click_element(FunctionsLocators.DESIGN_ORDER)

    @allure.step('Проверить появление окна заказа')
    def check_order(self):
        return self.check_displaying_element(FunctionsLocators.START_ORDER)

    @allure.step('Получить ссылку текущей страницы')
    def check_url(self):
        return self.get_url()




