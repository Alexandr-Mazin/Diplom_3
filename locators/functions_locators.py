from selenium.webdriver.common.by import By

class FunctionsLocators:
    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[contains(text(),"Конструктор")]')

    # Кнопка Лента заказов
    BUTTON_FEED = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')

    # Заголовок Лента заказов
    TITLE_FEED_ORDER = (By.XPATH, '//h1[contains(text(),"Лента заказов")]')

    # Ингредиент Флюоресцентная булка R2-D3
    INGREDIENT_BUN = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Детали открытой карточки Флюоресцентная булка R2-D3
    INGREDIENT_BUN_INFO = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')

    # Кнопка закрытия окна ингредиента
    INGREDIENT_CLOSED = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close_modified__3V5XS")]')

    # Область создания бургера
    BURGER_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # Счётчик у булочки
    COUNT_INGREDIENT = (By.XPATH,'.//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[@class="counter_counter__num__3nue1"][1]')

    # Кнопка Войти в аккаунт
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')

    # Поле Email на форме входа
    LOGIN_NAME = (By.XPATH, '//input[@name="name"]')

    # Поле Пароль в форме входа
    PASSWORD_NAME = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка Оформить заказ
    DESIGN_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # Сообщение Ваш заказ начали готовить
    START_ORDER = (By.XPATH, '//p[contains(text(),"Ваш заказ начали готовить")]')
