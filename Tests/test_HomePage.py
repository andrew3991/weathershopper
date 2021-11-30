import pytest
from Pages.HomePage import HomePage
from time import sleep

@pytest.mark.usefixtures("init_driver")
class TestHomePage:

    def test_tip_info_appear(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_tip_info()
        flag = self.homePage.is_tip_shown()
        assert flag

    def test_go_page_moisturizers(self):
        title = 'The Best Moisturizers in the World!'
        self.homePage = HomePage(self.driver)
        self.homePage.click_moisturizers_button()
        header = self.homePage.get_moisturizers_title(self.driver.title)
        assert title == header

    def test_go_page_sunscreens(self):
        title = 'The Best Sunscreens in the World!'
        self.homePage = HomePage(self.driver)
        self.homePage.click_sunscreens_button()
        header = self.homePage.get_sunscreens_title(self.driver.title)
        assert title == header



