from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL, STANDARD_USER, LOCKED_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_TC01_standard_user_can_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    assert inventory_page.is_displayed()


def test_TC02_locked_out_user_cannot_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(LOCKED_USER, PASSWORD)

    error = login_page.get_error_message()

    assert "locked out" in error.lower()

    wait = WebDriverWait(driver, 5)

    wait.until(
        EC.url_contains("saucedemo.com")
    )

    assert "inventory.html" not in driver.current_url


def test_TC21_products_url_after_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    wait = WebDriverWait(driver, 15)
    wait.until(EC.url_contains("inventory.html"))

    wait.until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()

    wait.until(EC.visibility_of_element_located(LoginPage.USERNAME))

    driver.get(f"{BASE_URL}/inventory.html")

    wait.until(EC.visibility_of_element_located(LoginPage.USERNAME))

    assert "inventory.html" not in driver.current_url
