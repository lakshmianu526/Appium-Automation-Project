from appium.webdriver.common.appiumby import AppiumBy
from utils.driver import wait_for_element

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # Cart page elements
        self.cart_item_name = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/titleTV')  # Name in cart
        self.cart_item_price = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/priceTV')  # Price in cart

    def get_cart_item_details(self):
        name = wait_for_element(self.driver, self.cart_item_name).text
        price = wait_for_element(self.driver, self.cart_item_price).text
        return name, price