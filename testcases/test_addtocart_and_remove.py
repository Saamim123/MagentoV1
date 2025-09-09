from re import search

import pytest
import os

from pageobjects.Luma_Homepage import Luma_homepage
from pageobjects.Myaccountpage import Myaccountpage
from pageobjects.UserHomepage import UserHomepage
from pageobjects.search_result_page import SearchResult
from utilities.customlogger import CustomLogger
from utilities.readproperties import Readconfig

@pytest.mark.usefixtures("login_fixture")
class Test_addto_cart_and_remove_005:
    logger = CustomLogger().get_logger()
    driver=None

    def test_add_to_cart_and_remove(self):
        self.logger.info("--------starting add to cart and removal test")
        self.search_page=SearchResult(self.driver)
        self.lh=Luma_homepage(self.driver)
        self.lh.searchbox()
        self.lh.send_text()
        self.lh.click_search()

        self.search_page.click_add_to_cart()
        self.search_page.get_text_cnf()
        self.search_page.click_cart()
        self.search_page.delete_from_cart()
        self.search_page.removal_cnf_popup()
        conf_msg=self.search_page.get_removal_cnf_text()
        self.logger.info(f"Confirmation message received:{conf_msg}")

        #assertion
        assert "You have no items in your shopping cart." in conf_msg



