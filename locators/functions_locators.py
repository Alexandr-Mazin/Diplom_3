from selenium.webdriver.common.by import By

class FunctionsLocators:

    # Кнопка Конструктор
    button_constructor = (By.XPATH, '//p[contains(text(),"Конструктор")]')

    # Кнопка Лента заказов
    button_feed = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')

    # Заголовок Лента заказов
    title_feed_order = (By.XPATH, '//h1[contains(text(),"Лента заказов")]')

    # Ингредиент Флюоресцентная булка R2-D3
    ingredient_bun = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Детали открытой карточки Флюоресцентная булка R2-D3
    ingredient_bun_info = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')

    # Кнопка закрытия окна ингредиента
    ingredient_closed = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close_modified__3V5XS")]')

    # Область создания бургера
    burger_area = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # счётчик у булочки
    count_ingredient = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[''@class="counter_counter__num__3nue1"][1]')

    # Кнопка Войти в аккаунт
    login_button = (By.XPATH, '//button[contains(text(),"Войти")]')

    # Поле Email на форме входа
    login_name = (By.XPATH, '//input[@name="name"]')

    # Поле Пароль в форме входа
    password_name= (By.XPATH, '//input[@name="Пароль"]')

    # Поле Пароль в форме входа
    design_order = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # Сообщение Ваш заказ начали готовить
    start_order = (By.XPATH, '//p[contains(text(),"Ваш заказ начали готовить")]')


