import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    services = Service(executable_path='C:/Users/Анастасия/YandexProject/qa_python_tasks-main/chromedriver.exe')
    browser = webdriver.Chrome(service=services)
    browser.maximize_window()
    yield browser
    browser.quit()
