from appium.webdriver.common.appiumby import AppiumBy
from utils.driver import wait_for_element

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        # Menu navigation elements
        self.hamburger_icon = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/menuIV')
        self.catalog_menu_item = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/itemTV')  
        # Catalog page elements
        self.product_image = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/productIV') 
        self.sort_icon = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/sortIV')
        self.sort_price_ascending = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/priceAscCL')  
        self.product_price = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/priceTV')

    def navigate_to_catalog(self):
        wait_for_element(self.driver, self.hamburger_icon).click()
        wait_for_element(self.driver, self.catalog_menu_item).click()

    def click_product_image_by_name(self, product_name):
        # Find the ImageView corresponding to the product name using XPath
        xpath = f"//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/titleTV' and @text='{product_name}']/preceding-sibling::android.widget.ImageView[@resource-id='com.saucelabs.mydemoapp.android:id/productIV']"
        product_image = wait_for_element(self.driver, (AppiumBy.XPATH, xpath))
        product_image.click()

    def apply_sorting_by_price_ascending(self):
        wait_for_element(self.driver, self.sort_icon).click()
        wait_for_element(self.driver, self.sort_price_ascending).click()

    def get_product_prices(self):
        price_elements = self.driver.find_elements(*self.product_price)
        return [float(elem.text.replace("$", "").replace(" ", "")) for elem in price_elements if elem.text]