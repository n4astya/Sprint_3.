from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


class TestLogOutOfAccount:
    def test_logout(self, driver):
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

        assert WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(L.log_enter))
