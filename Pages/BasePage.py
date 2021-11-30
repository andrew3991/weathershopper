from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator))
        return bool(element)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title

    def get_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(by_locator))
        return elements

    def new_frame(self, frameName):
        WebDriverWait(self.driver, 10).until(ec.frame_to_be_available_and_switch_to_it(frameName))

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)
