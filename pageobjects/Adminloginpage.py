
from selenium import webdriver
from selenium.webdriver.common.by import By


class AdminLogin:

    Username_txtbox_xpath="//input[@id='username']"
    Password_txtbox_xpath="//input[@id='login']"
    btn_signin_xpath="//span[normalize-space()='Sign in']"


    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):

        self.driver.find_element(By.XPATH,self.Username_txtbox_xpath).send_keys(username)

    def setpassword(self,password):

        self.driver.find_element(By.XPATH,self.Password_txtbox_xpath).send_keys(password)

    def clicksign(self):

        self.driver.find_element(By.XPATH,self.btn_signin_xpath).click()











