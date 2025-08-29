from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchResult:
    result_xpath="//a[contains(text(),'Fusion Backpack')]"
    add_to_wishlist_linktext="Add to Wish List"

    def __init__(self,driver):
        self.driver=driver
        self.wait=

    def click_result(self):
        self.driver.find_element(By.XPATH, self.result_xpath).click()

    def click_add_to_wishlist(self):
        self.driver.find_element(By.LINK_TEXT, self.add_to_wishlist_linktext).click()










