# Harvee Technologies — QA Automation Assessment

## Project Overview

This project contains manual test cases and automated UI tests for the Sauce Demo web application. The automation suite uses Python, Selenium WebDriver, and pytest.

The tests cover login, product sorting, cart operations, checkout field validation, and checkout total verification.

## Technology Stack

* Python 3.12
* Selenium WebDriver
* pytest
* pytest-html
* Chrome browser
* Page Object Model (POM)

## Project Structure

```text
Harvee_Tech/
├── tests/
│   ├── test_login.py
│   ├── test_sorting.py
│   ├── test_cart.py
│   └── test_checkout.py
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── config.py
├── conftest.py
├── A1_Manual_Test_Cases.md
└── README.md
```

## Prerequisites

* Python 3.12 or a compatible Python 3 version.
* Google Chrome installed.
* Internet access to reach the Sauce Demo application.

Selenium Manager normally handles ChromeDriver setup automatically when Selenium starts.

## Installation

Open a terminal in the project root directory.

Install the required packages:

```bash
python -m pip install selenium pytest pytest-html
```

## Configuration

The default configuration targets Sauce Demo.

The following environment variables can override the default values:

| Variable         | Purpose                  | Default                     |
| ---------------- | ------------------------ | --------------------------- |
| `BASE_URL`       | Application URL          | `https://www.saucedemo.com` |
| `STANDARD_USER`  | Standard test username   | `standard_user`             |
| `LOCKED_USER`    | Locked-out test username | `locked_out_user`           |
| `SAUCE_PASSWORD` | Shared test password     | `secret_sauce`              |

These are public demonstration credentials, not personal account credentials.

## Running the Tests

Run the entire test suite:

```bash
python -m pytest tests/ -v
```

Run only login tests:

```bash
python -m pytest tests/test_login.py -v
```

Run only checkout tests:

```bash
python -m pytest tests/test_checkout.py -v
```

Run checkout field-validation tests:

```bash
python -m pytest tests/test_checkout.py -k missing_checkout_fields -v
```

## Test Reporting

Generate an HTML report:

```bash
python -m pytest tests/ -v --html=report.html --self-contained-html
```

Generate a JUnit XML report:

```bash
python -m pytest tests/ -v --junitxml=report.xml
```

The generated report files are created in the project root directory.

## Automation Design

The project follows the Page Object Model:

* Page classes contain locators and page interactions.
* Test modules contain test scenarios and assertions.
* Configuration values are stored separately in `config.py`.
* Explicit waits are used to synchronize browser actions with page elements.
* pytest parameterization is used to test multiple checkout validation scenarios.
* Each test uses a separate WebDriver fixture.

## Current Automation Coverage

The current suite contains eight test executions covering:

* Standard user login.
* Locked-out user login.
* Product sorting by price from low to high.
* Adding products to the cart and removing one.
* Missing first name during checkout.
* Missing last name during checkout.
* Missing postal code during checkout.
* Completing checkout and verifying the order total.

The suite passed all eight tests in the latest recorded run. Results should be regenerated before final submission to confirm the current status.

## Manual-to-Automation Mapping

Refer to `A1_Manual_Test_Cases.md` for the manual test cases and the mapping between selected manual scenarios and their automation tests.

## Extending the Suite

Additional tests can be added by:

1. Identifying the manual test case and its expected behaviour.
2. Creating or updating the relevant Page Object.
3. Adding an independent pytest test.
4. Using explicit waits and stable locators.
5. Running the relevant test and the full regression suite.
6. Reviewing test failures and generated reports.

## Limitations

The current suite covers selected critical workflows, not every manual test case. Browser compatibility, accessibility, session-history behaviour, and other unautomated scenarios require additional validation.

## Disclaimer

Sauce Demo is used as a demonstration application for this assessment. Test results apply to the tested environment and the scenarios included in this project.
