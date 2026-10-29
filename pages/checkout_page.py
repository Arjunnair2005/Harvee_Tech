from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    CHECKOUT_OVERVIEW = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def continue_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def wait_until_overview_or_error(self):
        return self.wait.until(
            lambda driver: (
                driver.current_url.endswith("checkout-step-two.html")
                or driver.find_elements(*self.ERROR_MESSAGE)
            )
        )

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text

    def get_amount(self, locator):
        text = self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text
        return float(text.split("$")[-1])

    def finish_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def is_order_complete(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text == "Thank you for your order!"

    def is_on_overview_page(self):
        self.wait.until(
            EC.url_contains("checkout-step-two.html")
        )
        return self.driver.current_url.endswith("checkout-step-two.html")
