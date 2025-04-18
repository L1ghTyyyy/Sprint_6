import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = ""

    def get_page(self, url: str):
        self.driver.get(url)

    def wait_for_element_to_be_visible(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click_on(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    def send_keys(self, locator, text: str):
        element = self.wait_for_element_to_be_visible(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to(self, locator):
        element = self.wait_for_element_to_be_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return locator

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element(self, locator):
        return self.wait_for_element_to_be_visible(locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_page(self, url_contains: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_contains)
        )

    @allure.step("Переключиться на новую вкладку с URL, содержащим «{partial_url}»")
    def switch_to_new_window_with_url_contains(self, partial_url: str, timeout: int = 10):
        original = self.driver.current_window_handle
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(2)
        )
        new_window = [w for w in self.driver.window_handles if w != original][0]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )

    def get_current_url(self):
        return self.driver.current_url
