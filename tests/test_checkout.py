import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import STANDARD_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def start_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    wait = WebDriverWait(driver, 15)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    wait.until(EC.url_contains("inventory.html"))
    inventory_page.add_two_products()
    inventory_page.open_cart()

    wait.until(EC.url_contains("cart.html"))

    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    checkout_page = CheckoutPage(driver)
    checkout_page.wait.until(
        EC.visibility_of_element_located(CheckoutPage.FIRST_NAME)
    )
    return checkout_page


@pytest.mark.parametrize(
    ("first_name", "last_name", "postal_code", "expected_error"),
    [
        ("", "Nair", "641402", "First Name is required"),
        ("Arjun", "", "641402", "Last Name is required"),
        ("Arjun", "Nair", "", "Postal Code is required"),
    ],
)
def test_TC15_TC16_TC17_missing_checkout_fields(
    driver, first_name, last_name, postal_code, expected_error
):
    checkout_page = start_checkout(driver)

    checkout_page.enter_customer_details(
        first_name, last_name, postal_code
    )
    checkout_page.continue_checkout()
    checkout_page.wait_until_overview_or_error()

    assert expected_error in checkout_page.get_error_message()


def test_TC14_TC18_complete_checkout_and_verify_total(driver):
    checkout_page = start_checkout(driver)

    checkout_page.enter_customer_details("Arjun", "Nair", "641402")
    checkout_page.continue_checkout()

    assert checkout_page.is_on_overview_page()

    item_total = checkout_page.get_amount(CheckoutPage.ITEM_TOTAL)
    tax = checkout_page.get_amount(CheckoutPage.TAX)
    total = checkout_page.get_amount(CheckoutPage.TOTAL)

    assert total == pytest.approx(item_total + tax, abs=0.011)

    checkout_page.finish_checkout()
    assert checkout_page.is_order_complete()

    driver.find_element("id", "back-to-products").click()
    assert driver.find_elements("class name", "shopping_cart_badge") == []

