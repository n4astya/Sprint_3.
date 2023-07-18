from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


# переход к разделу «Булки»
def test_section_buns():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order))

    driver.find_element(*L.place_order).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

    driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
    driver.find_element(*L.password).send_keys('1998mama')
    driver.find_element(*L.enter).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.buns))

    driver.find_element(*L.buns).click()

    assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(L.buns_log))

    driver.quit()


# переход к разделу «Соусы»
def test_section_sauces():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    driver = webdriver.Chrome(service=services)

    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order))

    driver.find_element(*L.place_order).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

    driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
    driver.find_element(*L.password).send_keys('1998mama')
    driver.find_element(*L.enter).click()

    WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.sauces))

    driver.find_element(*L.sauces).click()

    assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(L.sauces_log))

    driver.quit()

# переход к разделу «Начинки»
def test_section_fillings():
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
        expected_conditions.presence_of_element_located(L.fillings))

    driver.find_element(*L.fillings).click()

    assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(L.fillings_log))

    driver.quit()
