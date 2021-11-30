from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.CartPage import CartPage

class CatalogPage(BasePage):
    ITEM = (By.XPATH, "//*[contains(text(), 'Add')]")
    CART_TITLE = (By.ID, 'cart')
    ITEMS = (By.CLASS_NAME, 'col-4')
    IMG = (By.TAG_NAME, 'img')
    ITEM_TITLE = (By.XPATH, '//p[@class="font-weight-bold top-space-10"]')
    ITEM_PRICE = (By.XPATH, "//*[contains(text(), 'Price')]")
    MOISTURIZERS_URL = '/moisturizer'
    SUNSCREENS_URL = '/sunscreen'

    # Page Actions

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL+url)

    def add_to_cart(self, item):
        self.do_click(item)

    def get_cart_title(self):
        cart_title = self.get_element_text(self.CART_TITLE)
        return cart_title

    def get_all_add_buttons(self):
        buttons = self.get_elements(self.ITEM)
        return buttons

    def go_to_cart(self):
        self.do_click(self.CART_TITLE)
        #return CartPage(self.driver)

    def get_all_items(self):
        return self.get_elements(self.ITEMS)

    def get_images_of_item(self):
        return self.get_elements(self.IMG)

    def get_price_of_item(self):
        return self.get_elements(self.ITEM_PRICE)

    def get_title_of_item(self):
        return self.get_elements(self.ITEM_TITLE)

