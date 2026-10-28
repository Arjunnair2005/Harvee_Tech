import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1366, 768)

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")

        if browser:
            os.makedirs("screenshots", exist_ok=True)

            filename = (
                item.nodeid
                .replace("/", "_")
                .replace("\\", "_")
                .replace("::", "_")
                .replace(" ", "_")
                + ".png"
            )

            screenshot_path = os.path.join(
                "screenshots", filename
            )

            try:
                browser.save_screenshot(screenshot_path)
                print(f"\nFailure screenshot saved: {screenshot_path}")
            except Exception as error:
                print(f"\nCould not capture screenshot: {error}")