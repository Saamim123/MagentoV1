from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage
from utilities.readproperties import Readconfig

class Luma_homepage(BasePage):

    searxhbox_ID=(By.ID,"search")
    search_btn=(By.XPATH,"//button[@title='Search']")
    logo_xpath=(By.XPATH,"//a[@aria-label='store logo']//img")
    search_item=Readconfig.get_search_item_name()

    def is_logo_present(self):
        try:
            return self.driver.find_element(*self.logo_xpath).is_displayed()
        except:
            return False

    def searchbox(self):
        self.click(self.searxhbox_ID)

    def send_text(self):
        self.type(self.searxhbox_ID,self.search_item)


    def click_search(self):
        self.click(self.search_btn)











