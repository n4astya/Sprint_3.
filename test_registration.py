from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


class TestRegistration:
    def test_registration_success(self, driver):
        faker = Faker()
        driver.get('https://stellarburgers.nomoreparties.site/register')

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.e_mail))

        driver.find_element(*L.e_mail).send_keys(faker.name())
        driver.find_element(*L.log_in_registration).send_keys(faker.email())
        driver.find_element(*L.password).send_keys(faker.password())
        driver.find_element(*L.enter_reg).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        assert WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(L.log_enter))

    def test_registration_not_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        faker = Faker()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.e_mail))

        driver.find_element(*L.e_mail).send_keys(faker.name())
        driver.find_element(*L.log_in_registration).send_keys(faker.email())
        driver.find_element(*L.password).send_keys('19')
        driver.find_element(*L.enter_reg).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        assert driver.find_element(*L.incorrect_password).text == 'Некорректный пароль'
