import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage:

    createaccount_link_text="Create an Account"
    create_new_cx_link_text="Create New Customer"

    def __init__(self,driver):
        self.driver=driver


    def click_create_account(self):
        mywait=WebDriverWait(self.driver, 10)
        mywait.until(EC.visibility_of_element_located((By.LINK_TEXT,self.createaccount_link_text))).click()

    def click_create_new_cx(self):
        mywait=WebDriverWait(self.driver, 10)
        mywait.until(EC.visibility_of_element_located((By.LINK_TEXT,self.createaccount_link_text))).click()


