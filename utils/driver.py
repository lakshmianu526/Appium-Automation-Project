from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.device_name = 'emulator-5554'
    options.app_package = 'com.saucelabs.mydemoapp.android'
    options.app_activity = '.view.activities.MainActivity'
    options.no_reset = True
    options.new_command_timeout = 3600
    options.connect_hardware_keyboard = True
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    return driver

def wait_for_element(driver, locator, timeout=20):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located(locator))

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True) 
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path