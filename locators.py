from selenium.webdriver.common.by import By


class LoginPageLocators:
    place_order = (By.XPATH, ".//main/section[2]/div/button") # Кнопка "Оформить заказ"
    name = (By.NAME, "name") # Поле login
    password = (By.NAME, "Пароль") # Поле пароля
    enter = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти"
    buns = (By.XPATH, ".//main / section[1] / div[1]") # Вкладка Булки
    buns_log = (By.XPATH, ".//main/section[1]/div[2]/h2[1]")
    sauces = (By.XPATH, ".//main/section[1]/div[1]/div[2]/span") # Вкладка Соусы
    sauces_log = (By.XPATH, ".//main/section[1]/div[2]/h2[2]")
    fillings = (By.XPATH, ".//main/section[1]/div[1]/div[3]/span") # Вкладка Начинки
    fillings_log = (By.XPATH, ".//main/section[1]/div[2]/h2[3]")
    pa = (By.XPATH, ".//nav/a/p") # Кнопка "Личный кабинет"
    entry_in_registration = (By.XPATH, ".//main/div/div/p/a") # Кнопка "Войти" на форме регистрации
    desingner = (By.XPATH, ".//p[text()='Конструктор']") # Конструктор
    logo = (By.XPATH, ".//header/nav/div/a") # Логотип
    prof = (By.XPATH, ".//main/div/nav/ul/li/a") # Вкладка профиль
    exite = (By.XPATH, ".//nav/ul/li[3]/button") # Выход
    e_mail = (By.XPATH, ".// main / div / form / fieldset[1] / div / div / input") # e-mail
    log_in_registration = (By.XPATH, ".//main/div/form/fieldset[2]/div/div/input") # Поле login
    incorrect_password = (By.XPATH, ".//main/div/form/fieldset[3]/div/p") # Ошибка ввода пароля
    enter_reg = (By.XPATH, ".//main/div/form/button")



