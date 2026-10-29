from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    TITLE = (By.CSS_SELECTOR, ".title")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ADD_BUTTONS = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove']")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        ).text == "Products"

    def sort_by_price_low_to_high(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        Select(dropdown).select_by_value("lohi")

    def get_product_prices(self):
        self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_PRICES)
        )
        prices = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(price.text.replace("$", "")) for price in prices]

    def add_two_products(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.ADD_BUTTONS)
        )
        buttons[0].click()
        buttons[1].click()

    def get_cart_badge_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
        except Exception:
            return 0
        return int(badge.text or 0)

    def get_cart_item_names(self):
        return [
            item.text for item in self.driver.find_elements(*self.ITEM_NAMES)
        ]

    def remove_one_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BUTTON)
        ).click()

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
