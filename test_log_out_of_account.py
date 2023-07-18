from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


def test_go_out():
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

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.exite))

    driver.find_element(*L.exite).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.e_mail))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()

