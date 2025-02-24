from locators.order_feed_locators import OrderLocators
from pages.base_page import BasePage
import allure
import time

class OrderFeed(BasePage):
    @allure.step('Ожидание кнопки Лента заказов')
    def wait_order_feed(self):
        self.wait_visibility_element(OrderLocators.button_order_feed)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_feed(self):
        self.click_element(OrderLocators.button_order_feed)

    @allure.step('Клик по заказу')
    def click_order_in_feed(self):
        self.click_element(OrderLocators.order_in_feed)

    @allure.step('Проверить наличие на странице окна заказа')
    def check_displaying_order_info(self):
        return self.check_displaying_element(OrderLocators.order_info)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_burger_area(self):
        source_element = self.driver.find_element(*OrderLocators.ingredient_bun)
        target_element = self.driver.find_element(*OrderLocators.burger_area)

        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Ожидание булочки')
    def wait_bun(self):
        self.wait_clickable_element(OrderLocators.burger_area)

    @allure.step('Вход в ЛК')
    def login_to_account(self, test_user):
        email = test_user["email"]
        password = test_user["password"]
        self.enter_text(OrderLocators.login_name, email)
        self.enter_text(OrderLocators.password_name, password)
        self.wait_clickable_element(OrderLocators.login_button)
        self.click_element(OrderLocators.login_button)

    @allure.step('Клик по созданию заказа')
    def click_order_create_button(self):
        self.click_element(OrderLocators.order_create_button)

    @allure.step('Клик по крестику закрытия окна с заказом')
    def click_order_exit_button(self):
        self.wait_clickable_element(OrderLocators.order_exit_button)
        time.sleep(3)
        self.click_element(OrderLocators.order_exit_button)

    @allure.step('Клик по Личный кабинет')
    def click_order_personal_account(self):
        self.wait_clickable_element(OrderLocators.personal_account)
        self.click_element(OrderLocators.personal_account)

    @allure.step('Клик по История заказов')
    def click_history_order(self):
        self.wait_clickable_element(OrderLocators.history_order)
        self.click_element(OrderLocators.history_order)


    @allure.step('Получить номер заказа из истории')
    def text_history_order_number(self):
        self.wait_clickable_element(OrderLocators.history_order_number)
        return self.get_text_element(OrderLocators.history_order_number)

    @allure.step('Получить номер заказа из истории')
    def text_feed_order_number(self):
        self.wait_clickable_element(OrderLocators.feed_order_number)
        return self.get_text_element(OrderLocators.feed_order_number)

    @allure.step('Получить количество заказов за всё время')
    def text_order_all_time(self):
        self.wait_clickable_element(OrderLocators.order_all_time)
        return self.get_text_element(OrderLocators.order_all_time)

    @allure.step('Получить количество заказов за сегодня')
    def text_order_today(self):
        self.wait_clickable_element(OrderLocators.order_today)
        return self.get_text_element(OrderLocators.order_today)

    @allure.step('Клик по Конструктор')
    def click_constractor(self):
        self.wait_clickable_element(OrderLocators.button_constructor)
        self.click_element(OrderLocators.button_constructor)

    @allure.step('Получить номер заказа после оформления')
    def text_order_number(self):
        self.wait_clickable_element(OrderLocators.order_number)
        time.sleep(3)
        return self.get_text_element(OrderLocators.order_number)

    @allure.step('Получить номер заказа в работе')
    def text_order_number_work(self):
        self.wait_clickable_element(OrderLocators.order_number_work)
        return self.get_text_element(OrderLocators.order_number_work)