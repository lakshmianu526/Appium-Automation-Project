import pytest
from utils.driver import get_driver
from datetime import datetime
import os
import logging

# Set up logging (optional, for better debugging)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def driver():
    driver_instance = get_driver()
    yield driver_instance
    driver_instance.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute the test and get the result
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')  # Get the driver from the test fixture
        if driver is None:
            logger.warning("Driver not found in test fixture, skipping screenshot.")
            return
        
        try:
            # Define screenshot directory
            screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            
            # Generate unique filename with timestamp and test name
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
            
            # Take and save screenshot
            driver.get_screenshot_as_file(screenshot_path)
            logger.info(f"Screenshot saved to: {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")