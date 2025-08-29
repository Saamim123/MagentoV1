from turtledemo.clock import setup

import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects import Adminloginpage
from pageobjects.Adminloginpage import AdminLogin
import os
from utilities.customlogger import CustomLogger
from pageobjects.admin_homepage import admin_homepage
from utilities.readproperties import Readconfig
from pageobjects.admin_dashboard import admin_dashboard


class Test_001_AdminLogin:


    Url=Readconfig.get_admin_login_url()
    email=Readconfig.admin_email()
    password = Readconfig.admin_pwd()
    Expected_title="Dashboard / Magento Admin"
    logger = CustomLogger().get_logger()  #creating logger instance


    @pytest.mark.regression
    def test_login_admin(self,setup):
        self.logger.info("-------Starting Admin Login Test----------")
        self.driver=setup
        self.logger.info(f"Opening URL: {self.Url}")
        self.driver.get(self.Url)

        self.driver.maximize_window()
        self.logger.info("----Entering login credentials-----")

        self.LP=AdminLogin(self.driver)
        self.logger.debug(f"Username entered: {self.email}")
        self.LP.set_username(self.email)
        self.LP.set_password(self.password)
        self.logger.info("Clicked on Sign In button")
        self.LP.click_login()
        self.logger.info("Waiting for dashboard page to load")
        assert self.LP.is_dashboard_displayed() is True

        """#--------1. validate dashboard message------------
        expected_dashboard_msg= "Dashboard"

        self.adminhomepage=admin_homepage(self.driver)
        self.admindashboard=admin_dashboard(self.driver)
        actual_dashboard_msg=self.admindashboard.is_dashboard_displayed()

        # --------2. validate admin dashboard page title------------
        expected_title="Dashboard / Magento Admin"
        actual_title=self.driver.title

        if expected_dashboard_msg in actual_dashboard_msg and  expected_title == actual_title:
            self.logger.info("******login test passed*******")
            assert True

        else:
            self.logger.error("******** Login Test Failed ********")
            self.logger.error(f"Expected Dashboard: {expected_dashboard_msg}, Got: {actual_dashboard_msg}")
            self.logger.error(f"Expected Title: {expected_title}, Got: {actual_title}")"""











