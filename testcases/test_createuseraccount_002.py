import pytest
import os


from pageobjects.Createuseraccount import CreateNewAccount
from pageobjects.UserHomepage import UserHomepage
from utilities.randomstring import generate_random_email
from utilities.customlogger import CustomLogger
from utilities.readproperties import Readconfig

@pytest.mark.usefixtures("setup")
class TestUserRegistration:

    url=Readconfig.get_user_login_url()
    fname=Readconfig.get_fname()
    lname=Readconfig.get_lname()
    password=Readconfig.get_password()
    cnf_paswd=Readconfig.get_password()
    logger = CustomLogger().get_logger()
    driver = None    #creating logger instance



    @pytest.mark.sanity
    def test_createaccount(self):

        self.logger.info("-------Starting user registration Test")

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.HP=UserHomepage(self.driver)
        self.HP.click_create_account()
        self.createaccount=CreateNewAccount(self.driver)
        self.logger.info("-----Entering user informations---")
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #self.wait = WebDriverWait(self.driver, 10)
        self.createaccount.enter_fname(self.fname)
        self.createaccount.enter_lname(self.lname)
        #self.createaccount.close_popup()
        self.createaccount.checkbox_newsletter()
        self.createaccount.checkbox_remoteshopping()
        self.email=generate_random_email()
        self.createaccount.set_email(self.email)
        #self.createaccount.set_email("wwdwdm@gmail.com")
        self.createaccount.set_password(self.password)
        self.createaccount.confirm_password(self.cnf_paswd)
        self.logger.info("------Creating new user account-----")
        self.createaccount.create_account()
        act_msg=self.createaccount.capture_cnf_text()
        expected_msg = "Thank you for registering with Main Website Store."
        self.logger.info(f"Actual msg displayed: {act_msg}")
        assert act_msg == expected_msg, f"Expected '{expected_msg}' but got '{act_msg}'"





























