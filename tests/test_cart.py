import pytest
import allure
from pages.catalog_page import CatalogPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from utils.driver import wait_for_element

@allure.feature("Cart")
def test_add_to_cart_and_verify(driver):
    catalog_page = CatalogPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)
    catalog_page.navigate_to_catalog()  
    target_product_name = "Sauce Labs Backpack"  
    catalog_page.click_product_image_by_name(target_product_name)  
    product_details_page.add_to_cart()  
    product_details_page.go_to_cart()  
    cart_name, cart_price = cart_page.get_cart_item_details()  
    assert cart_name == target_product_name, f"Expected product name '{target_product_name}', but got '{cart_name}'"
    expected_price = "$ 29.99"  
    assert cart_price == expected_price, f"Expected price '{expected_price}', but got '{cart_price}'"