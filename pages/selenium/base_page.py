from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url: str):
        self.driver.get(url)

    def wait_visible(self, locator: tuple[str, str]):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def wait_clickable(self, locator: tuple[str, str]):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator: tuple[str, str]):
        self.wait_clickable(locator).click()

    def fill(self, locator: tuple[str, str], value: str):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(value)

    def should_have_text(self, locator: tuple[str, str], text: str):
        element = self.wait_visible(locator)
        assert element.text == text

    def should_contain_text(self, locator: tuple[str, str], text: str):
        element = self.wait_visible(locator)
        assert text in element.text

    def should_be_visible(self, locator: tuple[str, str]):
        self.wait_visible(locator)

    def get_value(self, locator: tuple[str, str]) -> str | None:
        return self.wait_visible(locator).get_attribute("value")
