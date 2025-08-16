from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class admin_dashboard:
    myaccount_btn_xpath="//a[@title='My Account']"
    signout_btn_xpath="//a[normalize-space()='Sign Out']"
    dashboard_text_xpath="//h1[normalize-space()='Dashboard']"


    def __init__(self,driver):
        self.driver=driver

    def click_myaccount(self):
        self.driver.find_element(By.XPATH,self.myaccount_btn_xpath).click()

    def is_dashboard_displayed(self):
        dashboard=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.dashboard_text_xpath)))
        return dashboard.text

    def click_signout(self):
        self.driver.find_element(By.XPATH,self.signout_btn_xpath).click()








