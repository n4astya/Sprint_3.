from selenium.webdriver.common.by import By


class LoginPageLocators:
    place_order = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    place_order1 = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Оформить заказ"
    name = (By.NAME, "name")  # Поле login
    password = (By.NAME, "Пароль")  # Поле пароля
    enter = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти"
    buns = (By.XPATH, ".//span[text()='Булки']")  # Вкладка Булки
    buns_log = (By.XPATH, ".//h2[text()='Булки']")  # Раздел булки
    sauces = (By.XPATH, ".//span[text()='Соусы']")  # Вкладка Соусы
    sauces_log = (By.XPATH, ".//h2[text()='Соусы']")
    fillings = (By.XPATH, ".//span[text()='Начинки']")  # Вкладка Начинки
    fillings_log = (By.XPATH, ".//h2[text()='Начинки']")
    pa = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    entry_in_registration = (By.XPATH, ".//a[text()='Войти']")  # Кнопка "Войти" на форме регистрации
    desingner = (By.XPATH, ".//p[text()='Конструктор']")  # Конструктор
    logo = (By.XPATH, ".//header/nav/div/a")  # Логотип
    prof = (By.XPATH, ".//main/div/nav/ul/li/a")  # Вкладка профиль
    exite = (By.XPATH, ".//button[text()='Выход']")  # Выход
    e_mail = (By.XPATH, ".//input[@name='name']")  # имя при регистрации
    log_in_registration = (By.XPATH, ".//main/div/form/fieldset[2]/div/div/input")  # Поле login
    incorrect_password = (By.XPATH, ".//main/div/form/fieldset[3]/div/p")  # Ошибка ввода пароля
    enter_reg = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    log_enter = (By.XPATH, './/h2')



