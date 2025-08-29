import pytest
from pageobjects.CustomerLoginPage import CustomerLoginPage
from pageobjects.Myaccountpage import Myaccountpage
from utilities.readproperties import Readconfig
from utilities.customlogger import CustomLogger
from pageobjects.UserHomepage import UserHomepage
from pageobjects.Luma_Homepage import Luma_homepage
@pytest.mark.usefixtures("setup")
class Test_user_login_003:

    user_login_url=Readconfig.get_user_login_url()
    email=Readconfig.get_user_login_email()
    password=Readconfig.get_user_login_password()
    user_login_confirmation_msg=Readconfig.get_user_login_cnf_msg()
    logger=CustomLogger().get_logger()     #creating logging instance
    driver=None
    def test_login_user(self):
        self.logger.info("-------Starting user Login Test----------")
        self.logger.info(f"Opening URL: {self.user_login_url}")

        self.driver.get(self.user_login_url)
        self.driver.maximize_window()

        self.HP=UserHomepage(self.driver)
        self.HP.click_login()
        self.CXLP = CustomerLoginPage(self.driver)
        self.lh=Luma_homepage(self.driver)
        self.CXLP.set_useremail(self.email)
        self.CXLP.set_password(self.password)
        self.logger.info("------logging into user account-----")
        self.CXLP.click_login()
        self.MYACP=Myaccountpage(self.driver)
        self.lh.is_logo_present()




