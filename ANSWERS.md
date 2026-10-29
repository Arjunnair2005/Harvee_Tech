# Harvee Technologies — QA Automation Tester Assessment

## B1 — Review and Rewrite an AI-Generated Cart-Total Test

### Review

AI-generated automation code should be reviewed before it is accepted. For a cart-total test, I would check whether the test:

* Uses reliable locators and explicit waits.
* Calculates the expected item total from the selected products rather than trusting the displayed subtotal.
* Verifies that the displayed tax and final total are consistent.
* Uses appropriate numeric comparisons to account for currency rounding.
* Produces clear assertion messages when a check fails.
* Can run independently and repeatedly.

A test that checks only whether the displayed total equals the displayed subtotal plus tax may miss a defect if the subtotal itself is incorrect.

### Improved validation approach

1. Record the prices of the products selected for the cart.
2. Calculate the expected item subtotal independently.
3. Compare the calculated subtotal with the displayed item total.
4. Verify that the displayed final total equals the displayed item total plus tax, using the application's rounding rules.
5. Report which calculation failed if an assertion does not pass.

Example assertion logic:

```python
import pytest

expected_subtotal = sum(selected_product_prices)

assert displayed_subtotal == pytest.approx(
    expected_subtotal, abs=0.011
), (
    f"Subtotal mismatch: expected {expected_subtotal}, "
    f"received {displayed_subtotal}"
)

assert displayed_total == pytest.approx(
    displayed_subtotal + displayed_tax, abs=0.011
), (
    f"Total mismatch: subtotal {displayed_subtotal} "
    f"+ tax {displayed_tax} != total {displayed_total}"
)
```

The expected tax calculation should also be verified independently if the tax rules are documented. The tolerance must be appropriate for the application's currency-rounding rules.

The exact locators and setup should be adapted to the supplied application and test code.

## B2 — Evaluating AI-Generated Output

### Selected scenario: AI-generated checkout test cases

I would use AI to suggest test cases for an online checkout workflow, but I would not accept the suggestions without reviewing them.

I would score the output using four checks, each rated from 0 to 5.

| Check                   | What I would evaluate                                                                | Scoring approach                                        |
| ----------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| Accuracy                | Are the expected results consistent with the actual requirements?                    | 0 = incorrect; 5 = fully correct                        |
| Coverage                | Does it include positive, negative, boundary, and relevant failure scenarios?        | 0 = major gaps; 5 = comprehensive for the defined scope |
| Relevance               | Are the test cases specific to the checkout workflow and useful for finding defects? | 0 = irrelevant; 5 = highly relevant                     |
| Clarity and consistency | Are steps, test data, and expected results understandable and consistent?            | 0 = unclear or contradictory; 5 = clear and consistent  |

**Maximum score: 20.**

I would compare the generated cases against the requirements and existing test suite, identify missing scenarios, remove duplicates, and correct inaccurate expected results. I would also check whether the output introduces assumptions that have not been approved by the client.

I would repeat selected prompts to investigate inconsistent outputs. Any safety, privacy, or security concern would be reviewed separately rather than being accepted because of a high numerical score.

The final test cases would be reviewed and validated by the tester before implementation.

## B3 — Defect Report: Product Price Sorting

**Title:** [P1] Price low-to-high sorting displays products in the wrong order

**Environment**

* Application release: 4.2.0
* Browser: Google Chrome
* Feature: Products page
* Scenario: Price sorting from low to high

**Preconditions**
The user is logged in and the Products page displays multiple products with different prices.

**Steps to reproduce**

1. Open the Products page.
2. Select the price low-to-high sorting option.
3. Inspect the displayed product prices.

**Expected result**

Products should be ordered numerically from the lowest price to the highest price.

**Actual result**

A product priced at $29.99 appears before a product priced at $15.99, violating the selected sorting order.

**Impact**

Users may have difficulty comparing products by price. This reduces confidence in the sorting feature and may affect purchasing decisions.

**Severity:** Major functional defect.

**Priority:** P1, subject to the team's prioritization criteria and release impact.

**Evidence to attach**

* Screenshot showing the incorrect ordering.
* Browser and application release details.
* Reproduction steps and test timestamp.
* Relevant browser console or application logs, if available.

**Suggested investigation**

Check the sorting implementation, whether prices are treated as numbers rather than strings, and whether the displayed list is refreshed correctly after changing the sort option.

**Regression testing**

Test low-to-high and high-to-low sorting across the complete product list, including products with similar prices and prices containing different digit lengths.

## B4 — Client Release Update

The following message is under 150 words.

> Hello Team,
>
> During release validation, we identified an issue in version 4.2.0 where the product price low-to-high sorting option displays some products in the wrong order. We also observed intermittent failures in the checkout workflow that require further investigation.
>
> The sorting defect is reproducible in Chrome and has been documented with reproduction steps and supporting evidence. The checkout issue is being investigated to determine its frequency, impact, and root cause.
>
> I recommend that we assess both issues against the release acceptance criteria before approving deployment. The sorting fix should be verified with regression tests covering both price-sorting directions. The checkout workflow should be rerun repeatedly, with logs reviewed to investigate the intermittent failures.
>
> I will share an updated status after the investigation and retesting are complete. Any release decision should be based on the confirmed impact and agreed release criteria.
>
> Regards,
> QA Team

## C1 — Production Incident: Checkout Failures

**Incident:** Some users have reported that checkout has been failing since this morning.

### 1. Initial questions

I would establish the following:

* When did the failures begin, and which users are affected?
* Are all users affected or only specific accounts, browsers, devices, or payment methods?
* Does the failure occur before payment, during payment, or after order submission?
* Are orders being created even when the interface reports a failure?
* Were there recent deployments, configuration changes, or dependency outages?

### 2. Investigation

I would first reproduce the issue in a controlled environment without creating duplicate orders or making unintended real payments.

I would review:

* Application and server logs around the reported failure times.
* HTTP status codes and failed API requests.
* Error rates, latency, and relevant service-health dashboards.
* Recent deployments and configuration changes.
* Database and payment-service responses, where relevant.

I would compare successful and failed checkout attempts to identify a common pattern. I would also check whether the problem is limited to a particular stage of checkout.

### 3. Containment and communication

I would notify the responsible engineer and incident lead, communicate the known impact, and provide regular updates.

If the issue is linked to a recent release, I would recommend evaluating rollback or another approved mitigation with the responsible team. I would not make an unapproved production change.

I would prioritize preventing duplicate orders, incorrect charges, and loss of order data.

### 4. Resolution and prevention

After identifying and fixing the cause, I would verify the affected workflow and run relevant regression tests. I would monitor error rates after the fix and document the timeline, root cause, impact, mitigation, and preventive actions.

## C2 — Production Issue, Communication, and Prevention

As a fresher, I have not independently owned a production incident. I would therefore avoid presenting a hypothetical incident as personal professional experience.

A relevant example based on the checkout scenario is an intermittent failure during order submission.

**Potential impact:** Customers may be unable to complete purchases. If the order is created but the confirmation fails to appear, customers may retry and potentially create duplicate orders.

**Investigation:** I would correlate application logs, API responses, order records, and payment-service results to establish whether the failure occurs before or after order creation. I would also check recent changes and attempt to reproduce the issue safely.

**Client communication:** I would communicate the confirmed impact, affected workflow, investigation status, mitigation, and next update time. I would distinguish confirmed facts from hypotheses.

**Prevention:** Depending on the confirmed root cause, actions could include stronger integration tests, improved error handling, monitoring and alerting, and idempotent order submission to prevent duplicate processing.

**Retrospective:** The team should document the timeline, root cause, detection gaps, response effectiveness, and assigned follow-up actions. Each action should have an owner and target date.

The specific corrective actions would depend on evidence gathered during the incident rather than assumptions made before investigation.
