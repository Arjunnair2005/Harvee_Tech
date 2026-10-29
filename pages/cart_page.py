from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_LIST = (By.CLASS_NAME, "cart_list")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_item_count(self):
        self.wait.until(
            EC.visibility_of_element_located(self.CART_LIST)
        )
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_names(self):
        self.wait.until(
            EC.visibility_of_element_located(self.CART_LIST)
        )
        return [
            item.text for item in self.driver.find_elements(*self.ITEM_NAMES)
        ]

    def is_empty(self):
        return self.get_item_count() == 0