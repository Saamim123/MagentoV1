import pytest

from utilities.customlogger import CustomLogger
from utilities.readproperties import Readconfig
from pageobjects.search_result_page import SearchResult


@pytest.mark.usefixtures("login_fixture")
class Test_add_to_compare_006:
    logger = CustomLogger().get_logger()
    driver = None

    def test_add_to_compare(self,search_item_fixture):
        self.logger.info("--------starting add to cart and removal test")
        self.search_result=SearchResult(self.driver)
        self.search_result.click_add_to_comparision()
        cnf_msg=self.search_result.click_add_to_comparision_cnf_msg()
        self.logger.info(f"Confirmation message received:{cnf_msg}")
        assert cnf_msg is not None, "❌ add to compare confirmation message not found"
        assert "You added product Bruno Compete Hoodie-XL-Black to the" in cnf_msg



