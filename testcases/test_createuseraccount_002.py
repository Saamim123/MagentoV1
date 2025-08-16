import pytest
import os

from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.Createuseraccount import create_new_account
from pageobjects.Homepage import Homepage
from utilities.randomstring import generate_random_email
from utilities.customlogger import CustomLogger
from utilities.readproperties import Readconfig


class Test_createaccount_002:

    url=Readconfig.get_user_login_url()
    fname=Readconfig.get_fname()
    lname=Readconfig.get_lname()
    password=Readconfig.get_password()
    cnf_paswd=Readconfig.get_password()
    logger = CustomLogger().get_logger()  #creating logger instance

    @pytest.mark.sanity
    def test_createaccount(self,setup):

        self.logger.info("-------Starting user registration Test")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.HP=Homepage(self.driver)
        self.HP.click_create_account()
        self.createaccount=create_new_account(self.driver)
        self.logger.info("-----Entering user informations---")
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait = WebDriverWait(self.driver, 10)
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
        actual_msg=self.createaccount.capture_cnf_text()
        print(f"Actual message: {repr(actual_msg)}")

        expected_msg="Thank you for registering with Main Website Store."



        if actual_msg==expected_msg:
            assert True
        else:
            self.logger.error("-----Account registartion failed----")
            assert False





















