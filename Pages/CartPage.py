from time import sleep

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData


class CartPage(BasePage):
    CART_TITLE = 'Cart items'
    PAY_BUTTON = (By.XPATH, '//button[@class="stripe-button-el"]')
    EMAIL = (By.XPATH, '//input[@id="email"]')
    CARD_NUMBER = (By.XPATH, '//input[@id="card_number"]')
    DATE = (By.XPATH, '//input[@id="cc-exp"]')
    CVC = (By.XPATH, '//input[@id="cc-csc"]')
    PLZ = (By.XPATH, '//input[@id="billing-zip"]')
    PAY_BUTTON_LAST = (By.TAG_NAME, 'button')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="container top-space-50"]//h2')
    MODAL = (By.XPATH, '//iframe[@name="stripe_checkout_app"]')

    # Page Actions

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL + '/cart')

    def get_cart_title(self, title):
        return self.get_title(title)

    def click_pay_button(self):
        self.do_click(self.PAY_BUTTON)

    def click_pay_button_last(self):
        self.do_click(self.PAY_BUTTON_LAST)

    def go_to_new_frame(self):
        self.new_frame(self.MODAL)

    def do_purchase(self, email, card, date, year, cvc, plz):

        self.send_keys(self.EMAIL, email)

        self.send_keys(self.CARD_NUMBER, card)
        self.send_keys(self.CARD_NUMBER, card)
        self.send_keys(self.CARD_NUMBER, card)
        self.send_keys(self.CARD_NUMBER, card)

        self.send_keys(self.DATE, date)
        self.send_keys(self.DATE, year)

        self.send_keys(self.CVC, cvc)
        self.send_keys(self.PLZ, plz)
        self.do_click(self.PAY_BUTTON_LAST)

    def get_success_message(self):
        success = self.get_element_text(self.SUCCESS_MESSAGE)
        return success