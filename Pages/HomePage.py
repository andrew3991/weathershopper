from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.CatalogPage import CatalogPage
from Config.config import TestData


class HomePage(BasePage):
    TIP = (By.CLASS_NAME, 'octicon-info')
    INFO = (By.CLASS_NAME, 'popover')
    TITLE = (By.TAG_NAME, 'title')
    MOISTURIZERS = (By.LINK_TEXT, 'Buy moisturizers')
    SUNSCREENS = (By.LINK_TEXT, 'Buy sunscreens')

    # Page Actions


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_tip_info(self):
        self.do_click(self.TIP)

    def click_moisturizers_button(self):
        self.do_click(self.MOISTURIZERS)
        return CatalogPage(self.driver, '/moisturizer')

    def click_sunscreens_button(self):
        self.do_click(self.SUNSCREENS)
        return CatalogPage(self.driver, '/sunscreen')

    def is_tip_shown(self):
        info = self.is_enabled(self.INFO)
        return info

    def get_moisturizers_title(self, title):
        return self.get_title(title)

    def get_sunscreens_title(self, title):
        return self.get_title(title)
