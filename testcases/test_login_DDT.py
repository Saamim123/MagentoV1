import os.path

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.Adminloginpage import AdminLogin
from pageobjects.admin_homepage import admin_homepage
from utilities.readproperties import Readconfig
from utilities.customlogger import CustomLogger
from utilities import xlutils
from pageobjects.admin_dashboard import admin_dashboard
import time
class Test_003_DDTlogin:

    url=Readconfig.get_admin_login_url()
    logger=CustomLogger().get_logger()
    path=os.path.abspath(os.curdir)+"\\testdata\\Magento_LoginData.xlsx"
    Expected_title = "Dashboard / Magento Admin"

    def test_login_admin_DDT(self,setup):
        self.logger.info("-------Starting Admin Login Test----------")
        self.rows=xlutils.getRowCount(self.path,"Sheet1")
        lst_status=[]
        self.driver = setup
        self.logger.info(f"Opening URL: {self.url}")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.ad=admin_dashboard(self.driver)
        self.adminhomepage = admin_homepage(self.driver)
        self.admindashboard = admin_dashboard(self.driver)



        self.LP = AdminLogin(self.driver)

        for r in range(2, self.rows + 1):
            time.sleep(15)
            self.email = xlutils.readData(self.path, "Sheet1", r, 1)
            self.password = xlutils.readData(self.path, "Sheet1", r, 2)
            self.exp = xlutils.readData(self.path, "Sheet1", r, 3)

            self.logger.info(f"---- Test iteration {r - 1} ----")
            self.LP.setusername(self.email)
            self.LP.setpassword(self.password)
            self.LP.clicksign()
            actual_dashboard_msg = self.admindashboard.is_dashboard_displayed()
            if self.exp=="Valid":
                if actual_dashboard_msg=="Dashboard":
                    lst_status.append('Pass')
                    self.admindashboard.click_myaccount()
                    self.admindashboard.click_signout()
                else:
                    lst_status.append('Fail')
            elif self.exp=="Invalid":
                if actual_dashboard_msg=="Dashboard":
                    lst_status.append('Fail')
                    self.admindashboard.click_myaccount()
                    self.admindashboard.click_signout()
                else:
                    lst_status.append('Pass')

        #final validation
        if "Fail" not in lst_status:
            assert True

        else:
            assert False






