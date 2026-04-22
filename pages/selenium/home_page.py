from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.selenium.base_page import BasePage

class HomePage(BasePage):
    URL = "https://github.com/"
    SOLUTIONS_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Solutions' and @aria-expanded]",
    )
    RESOURCES_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Resources' and @aria-expanded]",
    )

    def open(self, url: str | None = None):
        super().open(url or self.URL)

    def open_solutions_menu(self):
        button = self.wait_visible(self.SOLUTIONS_BUTTON)
        ActionChains(self.driver).move_to_element(button).perform()
        if button.get_attribute("aria-expanded") != "true":
            self.click(self.SOLUTIONS_BUTTON)

    def open_resources_menu(self):
        button = self.wait_visible(self.RESOURCES_BUTTON)
        ActionChains(self.driver).move_to_element(button).perform()
        if button.get_attribute("aria-expanded") != "true":
            self.click(self.RESOURCES_BUTTON)
