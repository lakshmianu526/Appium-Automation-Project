import pytest
import allure
from pages.login_page import LoginPage
from utils.driver import get_driver, wait_for_element
from appium.webdriver.common.appiumby import AppiumBy

@allure.feature("Login")
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.enter_username("bod@example.com")
    login_page.enter_password("10203040")
    login_page.click_login()
    products_element = wait_for_element(driver, (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/productTV'))
    assert "Products" in products_element.text, "Login failed"

@allure.feature("Login")
def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_logout()
    login_page.logout()
    Login_element = wait_for_element(driver, (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/loginTV'))
    assert "Login" in Login_element.text, "Logout failed"
