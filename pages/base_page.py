import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    @allure.step('Принимаем экземпляр драйвера и сохраняем его в атрибут self.driver')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Создаем метод, который содержит в себе условное ожидание, пока элемент не станет видимым'
                 'и метод класса WebDriver - find_element')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Создаем метод, который содержит в себе условное ожидание, пока элемент не станет кликабильным'
                 'и выполяем клик, по элементу, с использованием метода класса WebDriver- find_element')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Создаем метод с и использованием метода класса WebDriver - end_keys, который добавляет текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Создаем метод, который использует метод класса find_element_with_wait для получения текста элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Созданием метод, который использует метод класса find_element_with_wait и get_attribute, для получения'
                 'атрибута элемента')
    def get_attribute_from_element(self, locator, type_attribute):
        return self.find_element_with_wait(locator).get_attribute(type_attribute)

    @allure.step('Создаем метод, который использует инструмент ожиания и условие, при котором,'
                 'элемент перестает отображаться на странице')
    def wait_until_close(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Создаем метод, который использует инструмент ожиания и условие, при котором,'
                 'происходит ожидание, пока значение одного элемента, не станет таким же, как значение второго элемента.')
    def to_be_present_in_element(self, locator_1, locator_2):
        WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element(locator_1, locator_2))

    @allure.step('Создаем метод, который зажимает кликом требуемый элемент и переносит его в целевую область на странице')
    def drug_and_drop(self, locator_1, locator_2):
        locator_1 = self.find_element_with_wait(locator_1)
        locator_2 = self.find_element_with_wait(locator_2)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(locator_1, locator_2).perform()

