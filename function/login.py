from element_info.login_page import LoginPage
import element_info.main_page

def test_login(url, username, password, driver):
    login = LoginPage(driver)
    login.open_url(url)
    login.input_username(username)
    login.input_password(password)
    login.click_login()

def test_logout(driver):
    mainpage = element_info.main_page.MainPage(driver)
    mainpage.click_userModular()
    mainpage.click_logout()
