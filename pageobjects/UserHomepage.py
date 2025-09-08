import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.BasePage import BasePage

class UserHomepage(BasePage):
    create_account_linktext=(By.LINK_TEXT, "Create an Account")
    login_linktext=(By.XPATH,"//div[@class='panel header']//a[contains(text(),'Sign In')]")


    #action

    def click_create_account(self):
        self.click(self.create_account_linktext)

    def click_login(self):
        self.click(self.login_linktext)
        










