from selenium.webdriver.common.by import By
class MainPageLocators:
    ENTER_TO_ACCOUNT_BUTTON = (By.XPATH, ".//div/button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and "
                                         "text()= 'Войти в аккаунт']")
    PERSONAL_ACCOUNT = (By.XPATH, ".//header//a/p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and contains(text(), 'Личный Кабинет')]")
    ORDER_NUMBER = (By.XPATH, ".//div/p[text()= 'идентификатор заказа']")
    ORDER_LIST_TAB = (By.XPATH, ".//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Лента Заказов')]")

    CONSTRUCTOR_TAB = (By.XPATH, ".//div//p[text() = 'Конструктор']")
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']")
    INGREDIENT = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3' and @class = 'BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4']")
    INGREDIENT_DETAILS = (By.XPATH, ".//div/h2[text() = 'Детали ингредиента']")
    CLOSE_BUTTON = (By.XPATH, ".//div/button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")
    MODAL_TITLE = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(text(), 'Детали ингредиента')]")
    COUNTER = (By.XPATH, ".//div/p[text() = '2']")
    CONSTRUCTOR_ELEMENT = (By.XPATH, ".//span[text() = 'Перетяните булочку сюда (верх)']")
    BUN = (By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//div//div/button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' "
                              "and text() = 'Оформить заказ']")
    ORDER_MODAL = (By.XPATH, ".//p[@class = 'undefined text text_type_main-medium mb-15' and text() = 'идентификатор заказа']")