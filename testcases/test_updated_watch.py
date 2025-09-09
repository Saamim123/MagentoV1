import pytest
from utilities.customlogger import CustomLogger
from utilities.readproperties import Readconfig
from pageobjects.Luma_Homepage import Luma_homepage


@pytest.mark.usefixtures("login_fixture")

class TestWatchesCategory_007:
    logger=CustomLogger().get_logger()
    driver=None

    def test_updated_watches_list(self):
        self.logger.info("----starting updated_watches_list Test----")
        self.lh=Luma_homepage(self.driver)
        self.lh.hover_on_update()
        self.lh.click_watches()
        item_list= self.lh.return_elements()
        assert item_list, "❌ No watches found in the category"


        for i in item_list:
            self.logger.info(f"Found item: {i.text}")
        self.logger.info("✅ Watches List Test completed successfully")
