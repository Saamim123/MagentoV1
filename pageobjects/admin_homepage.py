from selenium import webdriver
from selenium.webdriver.common.by import By


class admin_homepage:
    popup_btn_xpath="//aside[@class='modal-popup modal-system-messages _show']//button[@type='button']"

    def __init__(self,driver):
        self.driver=driver

    def click_popup(self):
        self.driver.find_element(By.XPATH,self.popup_btn_xpath).click()