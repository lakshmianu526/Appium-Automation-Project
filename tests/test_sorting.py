import pytest
import allure
from pages.catalog_page import CatalogPage
from utils.driver import wait_for_element



@allure.feature("Sorting")
def test_sort_by_price_ascending(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.navigate_to_catalog()
    catalog_page.apply_sorting_by_price_ascending()
    prices = catalog_page.get_product_prices()
    sorted_prices = sorted(prices)
    assert prices == sorted_prices, f"Prices are not in ascending order. Expected {sorted_prices}, but got {prices}"