from appium.webdriver.common.appiumby import AppiumBy
from utils.driver import wait_for_element

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Main page navigation elements
        self.hamburger_icon = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/menuIV')
        self.login_menu_item = (AppiumBy.ACCESSIBILITY_ID, 'Login Menu Item')
        # Login page elements
        self.username = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/nameET')
        self.password = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/passwordET')
        self.login_btn = (AppiumBy.ACCESSIBILITY_ID, 'Tap to login with given credentials')
        self.logout_menu_btn = (AppiumBy.ACCESSIBILITY_ID, 'Logout Menu Item')
        self.logout_btn = (AppiumBy.ID, 'android:id/button1')
        self.error_msg = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/errorTextField')  

    def navigate_to_login(self):
        wait_for_element(self.driver, self.hamburger_icon).click()
        wait_for_element(self.driver, self.login_menu_item).click()

    def navigate_to_logout(self):
        wait_for_element(self.driver, self.hamburger_icon).click()
        wait_for_element(self.driver, self.logout_menu_btn).click()

    def enter_username(self, username):
        elem = wait_for_element(self.driver, self.username)
        elem.send_keys(username)

    def enter_password(self, password):
        elem = wait_for_element(self.driver, self.password)
        elem.send_keys(password)

    def click_login(self):
        wait_for_element(self.driver, self.login_btn).click()

    def get_error_message(self):
        return wait_for_element(self.driver, self.error_msg).text

    def logout(self):
        wait_for_element(self.driver, self.logout_btn).click()