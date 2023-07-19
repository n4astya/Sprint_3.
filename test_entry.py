from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


# Вход через «Войти в аккаунт» на главной
def test_entry_with_entry_in_account():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order))

    driver.find_element(*L.place_order).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

    driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
    driver.find_element(*L.password).send_keys('1998mama')
    driver.find_element(*L.enter).click()

    WebDriverWait(driver, 4).until(
        expected_conditions.presence_of_element_located(L.place_order))

    assert driver.find_element(*L.place_order).text == 'Оформить заказ'

    driver.quit()


# Вход через «Личный кабинет» на главной
def test_entry_with_pa():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

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

    driver.quit()


# вход через кнопку в форме регистрации
def test_entry_with_button_in_registration():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

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

    driver.quit()


# вход через кнопку в форме восстановления пароля
def test_entry_with_button_in_password_uprising():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.entry_in_registration))

    driver.find_element(*L.entry_in_registration).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

    driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
    driver.find_element(*L.password).send_keys('1998mama')
    driver.find_element(*L.enter).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order))

    assert driver.find_element(*L.place_order).text == 'Оформить заказ'

    driver.quit()
