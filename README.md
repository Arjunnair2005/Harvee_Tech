# Harvee Technologies — QA Automation Assessment

## Project Overview

This project contains a set of manual QA test cases and automated UI tests for the Sauce Demo website. The goal is to validate the main customer flow in a realistic browser-based test environment using Python, Selenium WebDriver, and pytest.

The suite focuses on the critical user journeys: logging in, sorting products, managing the cart, validating checkout form errors, completing a purchase, and confirming the logout flow.

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

The project follows a simple Page Object Model approach:

* Page classes hold the locators and reusable interaction methods.
* Test modules contain the actual user flows and assertions.
* Configuration values live in `config.py` so the suite stays environment-driven.
* Explicit waits are used to handle timing issues and avoid flaky tests.
* pytest parameterization is used for the checkout validation scenarios.
* Each test gets its own browser instance through the shared driver fixture.

## Current Automation Coverage

The suite currently covers the main validation paths for this assessment, including:

* Standard user login.
* Locked-out user login.
* Product sorting by price from low to high.
* Adding products to the cart and removing one item.
* Checkout validation for missing first name, last name, and postal code.
* Completing checkout and confirming the total is correct.
* Logging out and confirming the protected page is no longer accessible.

The suite has been run and verified in the current project state.

## Manual-to-Automation Mapping

The manual scenarios are documented in `A1_Manual_Test_Cases.md`, and the automated tests mirror the key user journeys from that checklist.

## Extending the Suite

If more scenarios need to be added, the usual flow is:

1. Identify the relevant manual test case and expected behavior.
2. Update or create the corresponding Page Object.
3. Add a focused pytest test for the scenario.
4. Use explicit waits and stable selectors.
5. Run the targeted test and then the regression suite.
6. Review any failures and adjust the automation based on the real browser behavior.

## Limitations

This suite covers the most important workflows for the assessment rather than every possible browser or edge-case scenario. Some areas, such as broader browser compatibility, accessibility checks, and session edge cases, would need additional validation outside the current scope.

## Disclaimer

Sauce Demo is used as a demonstration app for this assessment. The results reflect the tested environment and the scenarios included in this project.
