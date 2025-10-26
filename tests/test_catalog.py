import pytest
import allure
from pages.catalog_page import CatalogPage
from pages.product_details_page import ProductDetailsPage
from utils.driver import wait_for_element

@allure.feature("Catalog")
def test_open_catalog_and_verify_product_details(driver):
    catalog_page = CatalogPage(driver)
    product_details_page = ProductDetailsPage(driver)
    catalog_page.navigate_to_catalog()  
    target_product_name = "Sauce Labs Backpack"  
    catalog_page.click_product_image_by_name(target_product_name)  
    details_name, details_price = product_details_page.get_product_details()  
    assert details_name == target_product_name, f"Expected product name '{target_product_name}', but got '{details_name}'"
    expected_price = "$ 29.99" 
    assert details_price == expected_price, f"Expected price '{expected_price}', but got '{details_price}'"