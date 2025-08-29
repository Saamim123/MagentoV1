
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self,driver,timeout=10):
        self.driver=driver
        self.mywait=WebDriverWait(driver,timeout)
        self.actions=ActionChains(driver)

        #core actions#

    def click(self,locator):
        self.mywait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def type(self,locator, text):
        self.mywait.until(EC.visibility_of_element_located(locator))
        element=self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        self.mywait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def is_displayed(self,locator):
        try:
            element=self.mywait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            return False

    def get_attribute(self,locator,attr_name):
        self.mywait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).get_attribute(attr_name)

    #wait helpers#
    def wait_for_url(self,url_fragment):
        self.mywait.until(EC.url_contains(url_fragment))

    def wait_for_alert(self):
        self.mywait.until(EC.alert_is_present())

    # ---------- Browser Helpers ---------- #


    def refresh_page(self):
        self.driver.refresh()

    #dropdowns#

    def select_by_visible_text(self,locator,text):
        element=self.driver.find_element(*locator)
        Select(element).select_by_visible_text(text)

    #Actions

    def hover(self,locator):
        element = self.driver.find_element(*locator)
        self.actions.move_to_element(element).perform()

    def double_click(self, locator):
        element = self.driver.find_element(*locator)
        self.actions.double_click(element).perform()



