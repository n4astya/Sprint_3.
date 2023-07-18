from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


def test_go_to_designer():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.pa))

    driver.find_element(*L.pa).click()

    driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
    driver.find_element(*L.password).send_keys('1998mama')
    driver.find_element(*L.enter).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.pa))

    driver.find_element(*L.pa).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.desingner))

    driver.find_element(*L.desingner).click()

    WebDriverWait(driver, 4).until(
        expected_conditions.presence_of_element_located(L.place_order))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_go_to_logo():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.pa))

    driver.find_element(*L.pa).click()

    driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
    driver.find_element(*L.password).send_keys('1998mama')
    driver.find_element(*L.enter).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.pa))

    driver.find_element(*L.pa).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.logo))

    driver.find_element(*L.logo).click()

    WebDriverWait(driver, 4).until(
        expected_conditions.presence_of_element_located(L.place_order))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()
