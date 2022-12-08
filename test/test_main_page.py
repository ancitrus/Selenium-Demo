from page.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    """" Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес"""
    page = MainPage(browser, link)
    """ Открываем страницу """
    page.open()
    """ Выполняем метод страницы """
    page.go_to_login_page()


# def go_to_login_page(browser):
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

