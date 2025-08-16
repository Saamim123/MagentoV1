from selenium import webdriver
from selenium.webdriver.common.by import By


class myaccountpage:

    logout_dropdown_xpath="//span[@class='customer-name active']//button[@type='button']"
    logout_linktext="Sign Out"

    def __init__(self,driver):
        self.driver=driver

    def click_dropdown(self):

        self.driver.find_element(By.XPATH,self.logout_dropdown_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linktext).click()

