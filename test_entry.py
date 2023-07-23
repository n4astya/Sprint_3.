'''from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


class TestEntry:
    # Вход через «Войти в аккаунт» на главной
    def test_entry_with_entry_in_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order1))

        driver.find_element(*L.place_order1).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
        driver.find_element(*L.password).send_keys('1998mama')
        driver.find_element(*L.enter).click()

        WebDriverWait(driver, 4).until(
            expected_conditions.presence_of_element_located(L.place_order))

        assert driver.find_element(*L.place_order).text == 'Оформить заказ'

    # Вход через «Личный кабинет» на главной
    def test_entry_with_pa(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.pa))

        driver.find_element(*L.pa).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
        driver.find_element(*L.password).send_keys('1998mama')
        driver.find_element(*L.enter).click()

        WebDriverWait(driver, 4).until(
            expected_conditions.presence_of_element_located(L.place_order))

        assert driver.find_element(*L.place_order).text == 'Оформить заказ'

    # вход через кнопку в форме регистрации
    def test_entry_with_button_in_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.entry_in_registration))

        driver.find_element(*L.entry_in_registration).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
        driver.find_element(*L.password).send_keys('1998mama')
        driver.find_element(*L.enter).click()

        WebDriverWait(driver, 4).until(
            expected_conditions.presence_of_element_located(L.place_order))

        assert driver.find_element(*L.place_order).text == 'Оформить заказ'

    # вход через кнопку в форме восстановления пароля
    def test_entry_with_button_in_password_uprising(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.entry_in_registration))

        driver.find_element(*L.entry_in_registration).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
        driver.find_element(*L.password).send_keys('1998mama')
        driver.find_element(*L.enter).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order))

        assert driver.find_element(*L.place_order).text == 'Оформить заказ'
'''