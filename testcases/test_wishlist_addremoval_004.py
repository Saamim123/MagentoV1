import pytest
from selenium import webdriver
from pageobjects.Myaccountpage import Myaccountpage
from pageobjects.UserHomepage import UserHomepage
from pageobjects.Luma_Homepage import Luma_homepage
from utilities.customlogger import CustomLogger
from utilities.readproperties import Readconfig

@pytest.mark.usefixtures("login_fixture")
class Test_wishlist_004:

    user_login_url=Readconfig.get_user_login_url()
    email=Readconfig.get_user_login_email()
    password=Readconfig.get_user_login_password()
    logger=CustomLogger().get_logger()
    driver=None

    def test_wish_list(self):
        self.logger.info("-------Starting wish list Test----------")
        self.driver.get(self.user_login_url)
        self.driver.maximize_window()
        self.logger.info("----Entering login credentials-----")
        self.lhp=Luma_homepage(self.driver)
        self.lhp.searchbox()
        self.lhp.send_text()
        self.lhp.click_search()
        self.macp=Myaccountpage(self.driver)
        self.macp.click_wish_icon()

        confirmation_msg = self.macp.wishlist_cnf_msg()
        self.logger.info(f"Confirmation message received: {confirmation_msg}")

        # Assertion
        assert confirmation_msg is not None, "❌ Wishlist confirmation message not found"
        assert "Bruno Compete Hoodie-XL-Black has been added to your Wish List. Click " in confirmation_msg, "❌ Wishlist confirmation text mismatch"
        self.logger.info("✅ Wishlist confirmation verified successfully")




