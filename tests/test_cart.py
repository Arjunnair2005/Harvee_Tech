from config import STANDARD_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_TC11_add_two_products_remove_one(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page.add_two_products()
    assert inventory_page.get_cart_badge_count() == "2"

    inventory_page.remove_one_product()
    assert inventory_page.get_cart_badge_count() == "1"

    inventory_page.open_cart()
    assert cart_page.get_item_count() == 1