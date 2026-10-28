from config import BASE_URL, STANDARD_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_TC08_products_sort_low_to_high(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    assert inventory_page.is_displayed()

    inventory_page.sort_by_price_low_to_high()
    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices), (
        f"Products are not sorted from low to high: {prices}"
    )