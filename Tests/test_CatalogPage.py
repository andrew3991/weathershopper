import pytest
from Pages.CatalogPage import CatalogPage
from Pages.HomePage import HomePage
from time import sleep


@pytest.mark.usefixtures("init_driver")
class TestCatalogPage:


    def test_add_item_to_cart(self):
        self.catalogPage = CatalogPage(self.driver, CatalogPage.SUNSCREENS_URL)
        buttons_list = self.catalogPage.get_all_add_buttons()
        for i in buttons_list:
            i.click()
            break
        cart_title = self.catalogPage.get_cart_title()
        assert '1 item(s)' == cart_title

    def test_items_have_all_info(self):
        self.catalogPage = CatalogPage(self.driver, CatalogPage.SUNSCREENS_URL)
        items = self.catalogPage.get_all_items()
        item_img = self.catalogPage.get_images_of_item()
        assert len(items) == len(item_img)
        item_title = self.catalogPage.get_title_of_item()
        assert len(items) == len(item_title)
        item_price = self.catalogPage.get_price_of_item()
        assert len(items) == len(item_price)

