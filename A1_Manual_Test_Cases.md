# A1 — Manual Test Suite

## 1. Questions and Assumptions

- Login validation

Question: Should the application show a clear error message for an invalid username, invalid password, or a locked-out account?
Assumption: Login should be rejected for invalid or locked-out user data, and the user should see a meaningful error message.

- Cart behaviour

Question: Can a customer add multiple quantities of the same product, or is each product limited to one entry in the cart?
Assumption: Each product is added once unless the application clearly supports quantity changes.

- Checkout validation

Question: What validation rules apply to first name, last name, and postal code? Are there restrictions on length, allowed characters, or format?
Assumption: All three fields are required. Empty values should trigger the appropriate validation message. Format checks should be tested only where the application or business requirements define them.

- Price calculation

Question: How is tax calculated and how should rounding be handled?
Assumption: The item total should match the sum of the displayed product prices, and the total should match item total plus tax according to the application's currency rules.

- Order cancellation

Question: Should cancelling checkout keep the cart contents intact?
Assumption: Cancelling checkout should not place an order and should return the customer to shopping without losing their cart contents accidentally.

- Session security

Question: What should happen if a logged-out customer tries to access a protected page through a saved URL or browser history?
Assumption: Protected pages should not reveal authenticated information to a logged-out user. The user should be redirected to login or otherwise denied access.

- Accessibility and supported devices

Question: Which browsers, viewport sizes, and accessibility standards should be supported?
Assumption: The main shopping flow should still be usable on common desktop and mobile sizes, with keyboard-friendly controls and clearly labeled form fields and errors.







## 2. Manual Test Cases

| ID   | Area                 | Type          | Title                                                  | Pre-conditions                                           | Steps                                                                                                | Test data                                                         | Expected result                                                                                            | Priority | Automate? and why                                                                      |
| ---- | -------------------- | ------------- | ------------------------------------------------------ | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------- |
| TC01 | Login                | Positive      | Standard user logs in                                  | User is on the login page                                | Enter valid credentials and click Login                                                              | `standard_user` / `secret_sauce`                                  | User reaches the Products page                                                                             | P1       | Yes — critical smoke test                                                              |
| TC02 | Login                | Negative      | Locked-out user attempts login                         | User is on the login page                                | Enter the locked-out user's credentials and click Login                                              | `locked_out_user` / `secret_sauce`                                | Login is rejected and an appropriate error appears                                                         | P1       | Yes — verifies account restrictions                                                    |
| TC03 | Login                | Negative      | Incorrect password                                     | User is on the login page                                | Enter a valid username and an incorrect password                                                     | `standard_user` / incorrect password                              | Login is rejected with an appropriate error                                                                | P1       | Yes — repeatable negative test                                                         |
| TC04 | Login                | Negative      | Empty login fields                                     | User is on the login page                                | Leave both fields empty and click Login                                                              | Empty username and password                                       | Login is rejected with a validation error                                                                  | P2       | Yes — validates required input                                                         |
| TC05 | Login                | Negative      | Empty password                                         | User is on the login page                                | Enter a username, leave the password empty, and click Login                                          | `standard_user` / empty password                                  | Login is rejected with an appropriate error                                                                | P2       | Yes — repeatable validation test                                                       |
| TC06 | Products             | Positive      | Sort products by name A to Z                           | Logged-in user is on the Products page                   | Select Name (A to Z) and inspect all product names                                                   | Available product list                                            | Product names appear in ascending alphabetical order                                                       | P1       | Yes — verifies the entire list                                                         |
| TC07 | Products             | Positive      | Sort products by name Z to A                           | Logged-in user is on the Products page                   | Select Name (Z to A) and inspect all product names                                                   | Available product list                                            | Product names appear in descending alphabetical order                                                      | P2       | Yes — repeatable sorting test                                                          |
| TC08 | Products             | Positive      | Sort products by price low to high                     | Logged-in user is on the Products page                   | Select Price (low to high) and inspect all prices                                                    | Available product prices                                          | Prices appear in ascending numerical order                                                                 | P1       | Yes — catches price-sorting defects                                                    |
| TC09 | Products             | Positive      | Sort products by price high to low                     | Logged-in user is on the Products page                   | Select Price (high to low) and inspect all prices                                                    | Available product prices                                          | Prices appear in descending numerical order                                                                | P2       | Yes — repeatable sorting test                                                          |
| TC10 | Cart                 | Positive      | Add one product                                        | Logged-in user is on the Products page                   | Click Add to cart for one product                                                                    | One available product                                             | Cart badge displays 1 and the product appears in the cart                                                  | P1       | Yes — core shopping workflow                                                           |
| TC11 | Cart                 | Positive      | Add two products and remove one from the Products page | Logged-in user is on the Products page                   | Add two different products and remove one                                                            | Two available products                                            | Badge decreases from 2 to 1 and only the remaining product is in the cart                                  | P1       | Yes — verifies cart state                                                              |
| TC12 | Cart                 | Positive      | Remove a product from the cart                         | Cart contains at least one product                       | Open the cart and click Remove for a product                                                         | One cart item                                                     | Product disappears from the cart and the badge updates correctly                                           | P2       | Yes — repeatable cart test                                                             |
| TC13 | Cart                 | Boundary      | Attempt checkout with an empty cart                    | User is logged in and has no cart items                  | Open the cart and attempt to proceed to checkout                                                     | Empty cart                                                        | No unintended order is created; behaviour follows the application's defined rules                          | P2       | No — expected behaviour needs clarification                                            |
| TC14 | Checkout             | Positive      | Complete a valid checkout                              | User is logged in and the cart contains a product        | Open the cart, click Checkout, enter all required fields, continue, inspect the overview, and finish | First name: Arjun; last name: Nair; postal code: 641402           | Order confirmation appears and the order is completed                                                      | P1       | Yes — end-to-end critical path                                                         |
| TC15 | Checkout             | Negative      | Missing first name                                     | Cart contains a product and the checkout form is open    | Leave first name empty, fill the other fields, and continue                                          | Empty first name; last name: Nair; postal code: 641402            | Checkout is blocked and a relevant validation error appears                                                | P1       | Yes — parameterized validation test                                                    |
| TC16 | Checkout             | Negative      | Missing last name                                      | Cart contains a product and the checkout form is open    | Fill first name and postal code, leave last name empty, and continue                                 | First name: Arjun; empty last name; postal code: 641402           | Checkout is blocked and a relevant validation error appears                                                | P1       | Yes — parameterized validation test                                                    |
| TC17 | Checkout             | Negative      | Missing postal code                                    | Cart contains a product and the checkout form is open    | Fill first and last names, leave postal code empty, and continue                                     | First name: Arjun; last name: Nair; empty postal code             | Checkout is blocked and a relevant validation error appears                                                | P1       | Yes — parameterized validation test                                                    |
| TC18 | Checkout             | Positive      | Verify order total                                     | Cart contains products and the checkout overview is open | Compare the displayed item total and tax, and calculate the final total                              | Two or more available products                                    | Displayed total equals item total plus tax, using the application's rounding rules                         | P1       | Yes — repeatable calculation test                                                      |
| TC19 | Checkout             | Positive      | Cancel checkout                                        | User has products in the cart and checkout is open       | Navigate to checkout and choose Cancel                                                               | One or more cart items                                            | No order is placed; the user returns to the appropriate page and cart state is preserved                   | P2       | Yes — verifies cancellation behaviour                                                  |
| TC20 | Checkout             | Boundary      | Minimum required field values                          | Cart contains a product and the checkout form is open    | Enter the shortest non-empty values permitted and continue                                           | One-character first and last names; shortest accepted postal code | Behaviour matches defined validation rules and no unexpected error occurs                                  | P2       | No — exact boundary rules require confirmation                                         |
| TC21 | Session security     | Security      | Open Products page after logout                        | User has logged in and then logged out                   | Enter the Products page URL directly in the browser                                                  | Products page URL                                                 | User cannot access protected content while logged out                                                      | P1       | Yes — security regression test                                                         |
| TC22 | Session security     | Security      | Use browser Back after logout                          | User has logged in, visited Products, and logged out     | Press the browser Back button                                                                        | Previously visited Products page                                  | Protected information is not exposed to the logged-out user                                                | P1       | Partially — browser caching may need manual investigation                              |
| TC23 | Usability            | Usability     | Check clarity of login and checkout errors             | User is on the login or checkout form                    | Trigger a validation error and inspect its visibility and wording                                    | Invalid login; missing checkout field                             | Error is visible, understandable, and associated with the relevant action or field                         | P2       | Partially — human review is useful for wording and clarity                             |
| TC24 | UI and compatibility | Compatibility | Check shopping workflow at a narrow viewport           | User is logged in using a supported browser              | Resize the viewport to a narrow mobile-sized width and navigate through products and cart            | Chrome; viewport approximately 375 × 812 pixels                   | Important controls remain visible and usable without unintended overlap or clipping                        | P2       | Partially — automate viewport checks and manually inspect usability                    |
| TC25 | Accessibility        | Accessibility | Keyboard navigation through login                      | User is on the login page                                | Use Tab and Enter to navigate and submit the form without a mouse                                    | Valid credentials                                                 | Login controls are keyboard accessible, focus is visible, and the form can be submitted using the keyboard | P2       | Partially — automate keyboard interactions and manually assess focus and accessibility |

### 2.1 Manual Testing Notes

* Test cases marked **Automated** have corresponding Selenium tests in the current automation suite.
* Test cases marked **Partially** require both automated checks and human evaluation.
* Test cases marked **No** need clarification or additional investigation before deciding on automation.
* Test cases that have not been automated should not be reported as executed or passed.
* The test data above is intended for the Sauce Demo test environment.







# Exploratory Testing Charter

Title: Explore the shopping journey using the problem user.

Timebox: 15 minutes.

Test account: `problem_user` with the shared practice-site password.

Aim: Investigate whether a user known to experience application problems can complete the shopping workflow and identify inconsistencies in the interface or functionality.

Steps:

1. Log in and inspect the Products page.
2. Check whether product images, names, descriptions, and prices match the displayed products.
3. Try both alphabetical and price-based sorting.
4. Add and remove products and verify the cart badge.
5. Navigate through checkout and inspect form behaviour.
6. Check whether the order overview reflects the selected products and their prices.

Evidence to collect: Screenshots, steps to reproduce each issue, expected behaviour, actual behaviour, and the browser and test-account details.

Completion criteria: Record the defects discovered, unexpected behaviour, areas explored, and any important areas not covered within the 15-minute timebox.

Constraint: Not to assume every observed difference is a defect. Compare actual behaviour with the business rules and record any unresolved requirement separately.




## 3. Testing Strategy

I would automate critical UI workflows, including valid and locked-out login, product sorting, cart operations, checkout validation, total calculations etc. These tests provide repeatable regression coverage for important customer journeys.If the application exposes suitable APIs, I would test cart calculations, checkout validation, and order processing at the API layer. Unit tests should cover isolated price, tax, rounding, and validation logic.
Manual testing would cover exploratory testing with problem users, usability, accessibility, browser compatibility, and unclear business rules.
The biggest remaining risk is an incorrect order or price calculation reaching production. I would prioritise verifying price totals, tax calculations, checkout completion, and order persistence, supported by appropriate API and end-to-end regression tests.


## Manual-to-Automation Mapping

| Manual Test Case | Scenario                            | Automation Test                                     | Status             |
| ---------------- | ----------------------------------- | --------------------------------------------------- | ------------------ |
| TC01             | Standard user login                 | `test_TC01_standard_user_can_login`                 | Automated — Passed |
| TC02             | Locked-out user login               | `test_TC02_locked_out_user_cannot_login`            | Automated — Passed |
| TC08             | Sort products by price, low to high | `test_TC08_products_sort_low_to_high`               | Automated — Passed |
| TC11             | Add two products and remove one     | `test_TC11_add_two_products_remove_one`             | Automated — Passed |
| TC14             | Complete checkout                   | `test_TC14_TC18_complete_checkout_and_verify_total` | Automated — Passed |
| TC15             | First name is required              | `test_TC15_TC16_TC17_missing_checkout_fields`       | Automated — Passed |
| TC16             | Last name is required               | `test_TC15_TC16_TC17_missing_checkout_fields`       | Automated — Passed |
| TC17             | Postal code is required             | `test_TC15_TC16_TC17_missing_checkout_fields`       | Automated — Passed |
| TC18             | Verify checkout total               | `test_TC14_TC18_complete_checkout_and_verify_total` | Automated — Passed |


### Automation Notes

* Selenium WebDriver with Python is used for browser automation.
* Pytest is used as the test runner.
* The Page Object Model separates page interactions from test logic.
* The checkout validation scenarios use pytest parameterization to execute multiple input combinations through one test function.
* Explicit waits are used to synchronize browser interactions with page elements.
* The full suite currently contains eight test executions, all passing in the latest run.
* Manual test cases not listed in this mapping have not yet been confirmed as automated.
