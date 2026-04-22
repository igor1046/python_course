from selenium.webdriver.common.by import By
from pages.selenium.base_page import BasePage

class ContactSalesPage(BasePage):
    FIRST_NAME = "John"
    LAST_NAME = "Doe"

    FIRST_NAME_INPUT = (
        By.XPATH,
        "//label[contains(normalize-space(), 'First name')]/following::input[1]"
        " | //input[contains(@name, 'first') or contains(@id, 'First')]",
    )
    LAST_NAME_INPUT = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Last name')]/following::input[1]"
        " | //input[contains(@name, 'last') or contains(@id, 'Last')]",
    )

    def fill_form(self):
        self.fill(self.FIRST_NAME_INPUT, self.FIRST_NAME)
        self.fill(self.LAST_NAME_INPUT, self.LAST_NAME)

    def check_filled_form(self):
        assert self.get_value(self.FIRST_NAME_INPUT) == self.FIRST_NAME
        assert self.get_value(self.LAST_NAME_INPUT) == self.LAST_NAME
