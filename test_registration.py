from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


def test_registration_success():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

    driver.get('https://stellarburgers.nomoreparties.site/register')

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.e_mail))

    driver.find_element(*L.e_mail).send_keys('n4asty1234')
    driver.find_element(*L.log_in_registration).send_keys('n4asty1234@yandex.ru')
    driver.find_element(*L.password).send_keys('1990mama1234')
    driver.find_element(*L.enter_reg).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()


def test_registration_not_success():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

    driver.get('https://stellarburgers.nomoreparties.site/register')

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.e_mail))

    driver.find_element(*L.e_mail).send_keys('n4asty123')
    driver.find_element(*L.log_in_registration).send_keys('n4asty123@yandex.ru')
    driver.find_element(*L.password).send_keys('19')
    driver.find_element(*L.enter_reg).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

    assert driver.find_element(*L.incorrect_password).text == 'Некорректный пароль'

    driver.quit()
