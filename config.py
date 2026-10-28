import os

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com"
)

STANDARD_USER = os.getenv(
    "STANDARD_USER",
    "standard_user"
)

LOCKED_USER = os.getenv(
    "LOCKED_USER",
    "locked_out_user"
)

PASSWORD = os.getenv(
    "SAUCE_PASSWORD",
    "secret_sauce"
)