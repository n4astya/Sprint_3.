'''from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators as L


class TestDesignerSection:
    # переход к разделу «Булки»
    def test_section_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order1))

        driver.find_element(*L.place_order1).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
        driver.find_element(*L.password).send_keys('1998mama')
        driver.find_element(*L.enter).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.pa))

        driver.find_element(*L.pa).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.desingner))

        driver.find_element(*L.desingner).click()

        assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(L.buns_log))

    # переход к разделу «Соусы»
    def test_section_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order1))

        driver.find_element(*L.place_order1).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
        driver.find_element(*L.password).send_keys('1998mama')
        driver.find_element(*L.enter).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.sauces))

        driver.find_element(*L.sauces).click()

        assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(L.sauces_log))

    # переход к разделу «Начинки»
    def test_section_fillings(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.place_order1))

        driver.find_element(*L.place_order1).click()

        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(L.name))

        driver.find_element(*L.name).send_keys('n4asty@yandex.ru')
        driver.find_element(*L.password).send_keys('1998mama')
        driver.find_element(*L.enter).click()

        WebDriverWait(driver, 4).until(
            expected_conditions.presence_of_element_located(L.fillings))

        driver.find_element(*L.fillings).click()

        assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(L.fillings_log))
'''