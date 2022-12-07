from pages.main_page import MainPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    """" Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес"""
    page = MainPage(browser, link)
    """ Открываем страницу """
    page.open()
    """ Выполняем метод страницы """
    page.go_to_login_page()


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()