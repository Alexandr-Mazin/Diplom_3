from selenium.webdriver.common.by import By

class OrderLocators:
    # Кнопка Лента заказов
    BUTTON_ORDER_FEED = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')

    # Заказ из списка
    ORDER_IN_FEED = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]')

    # Окно с заказом
    ORDER_INFO = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5")

    # Ингредиент Флюоресцентная булка R2-D3
    INGREDIENT_BUN = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Область создания бургера
    BURGER_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # Поле Email на форме входа
    LOGIN_NAME = (By.XPATH, '//input[@name="name"]')

    # Поле Пароль в форме входа
    PASSWORD_NAME = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка Оформить заказ
    DESIGN_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # Кнопка Войти в аккаунт
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')

    # Кнопка оформления заказа
    ORDER_CREATE_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # Кнопка закрытия оформления заказа
    ORDER_EXIT_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")

    # Кнопка личный кабинет
    PERSONAL_ACCOUNT = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]')

    # Кнопка история заказов
    HISTORY_ORDER = (By.XPATH, '//a[contains(text(),"История заказов")]')

    # Номер заказа в истории заказов
    HISTORY_ORDER_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-default']")

    # Номер заказа в ленте заказов
    FEED_ORDER_NUMBER = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]")

    # Выполнено за все время
    ORDER_ALL_TIME = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")

    # Выполнено за сегодня
    ORDER_TODAY = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")

    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[contains(text(),"Конструктор")]')

    # Номер заказа в окне после оформления
    ORDER_NUMBER = (By.XPATH,"//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'Modal_modal__title__2L34m')]")

    # Номер заказа в окне после оформления
    ORDER_NUMBER_WORK = (By.XPATH,"//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]")

