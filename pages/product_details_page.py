from appium.webdriver.common.appiumby import AppiumBy
from utils.driver import wait_for_element

class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        # Product details page elements
        self.product_details_name = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/productTV')  
        self.product_details_price = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/priceTV')  
        self.add_to_cart_button = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/cartBt') 
        self.cart_icon = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/cartRL') 

    def get_product_details(self):
        name = wait_for_element(self.driver, self.product_details_name).text
        price = wait_for_element(self.driver, self.product_details_price).text
        return name, price

    def add_to_cart(self):
        wait_for_element(self.driver, self.add_to_cart_button).click()

    def go_to_cart(self):
        wait_for_element(self.driver, self.cart_icon).click()