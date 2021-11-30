import pytest
from Pages.CatalogPage import CatalogPage
from Pages.HomePage import HomePage
from Pages.CartPage import  CartPage
from time import sleep


@pytest.mark.usefixtures("init_driver")
class TestCartPage:

    def test_go_to_cart_page(self):
        title = 'Cart Items'
        self.cartPage = CartPage(self.driver)
        self.catalogPage = CatalogPage(self.driver, CatalogPage.SUNSCREENS_URL)
        buttons_list = self.catalogPage.get_all_add_buttons()
        for i in buttons_list:
            i.click()
            break
        self.catalogPage.go_to_cart()
        header = self.cartPage.get_title(self.driver.title)
        assert title == header

    def test_buy_item(self):
        email = 'some@email.sm'
        card = '4242'
        date = '12'
        year = '23'
        cvc = '444'
        plz = '86159'
        title = 'Cart Items'
        success_message = 'PAYMENT SUCCESS'
        self.cartPage = CartPage(self.driver)
        self.catalogPage = CatalogPage(self.driver, CatalogPage.SUNSCREENS_URL)
        buttons_list = self.catalogPage.get_all_add_buttons()
        for i in buttons_list:
            i.click()
            break
        self.catalogPage.go_to_cart()
        self.cartPage.click_pay_button()
        self.cartPage.go_to_new_frame()
        self.cartPage.do_purchase(email, card, date, year, cvc, plz)
        self.cartPage.click_pay_button_last()
        msg = self.cartPage.get_success_message()

        assert msg == success_message
