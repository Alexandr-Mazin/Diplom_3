from selenium.webdriver.common.by import By

class OrderLocators:

    # Кнопка Лента заказов
    button_order_feed = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')

    # Заказ из списка
    order_in_feed = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]')

    # Окно с заказом
    order_info = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5")

    # Ингредиент Флюоресцентная булка R2-D3
    ingredient_bun = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Область создания бургера
    burger_area = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # Поле Email на форме входа
    login_name = (By.XPATH, '//input[@name="name"]')

    # Поле Пароль в форме входа
    password_name = (By.XPATH, '//input[@name="Пароль"]')

    # Поле Пароль в форме входа
    design_order = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # Кнопка Войти в аккаунт
    login_button = (By.XPATH, '//button[contains(text(),"Войти")]')

    # Кнопка оформления заказа
    order_create_button = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # Кнопка закрытия оформления заказа
    order_exit_button = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")

    # Кнопка личный кабинет
    personal_account = (By.XPATH, '// p[contains(text(), "Личный Кабинет")]')

    # Кнопка история заказов
    history_order = (By.XPATH, '//a[contains(text(),"История заказов")]')

    # Номер заказа в истории закзов
    history_order_number = (By.XPATH, "//p[@class='text text_type_digits-default']")

    # Номер заказа в ленте заказов
    feed_order_number = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]")

    # Выполнено за все время
    order_all_time = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")

    # Выполнено за сегодня
    order_today = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")

    # Кнопка Конструктор
    button_constructor = (By.XPATH, '//p[contains(text(),"Конструктор")]')

    # Номер заказа в окне после оформления
    order_number = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'Modal_modal__title__2L34m')]")

    # Номер заказа в окне после оформления
    order_number_work = (By.XPATH, "//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]")

