
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage



class AdminLogin(BasePage):

    Username_txtbox=(By.XPATH,"//input[@id='username']")
    Password_txtbox=(By.XPATH,"//input[@id='login']")
    btn_signin=(By.XPATH,"//span[normalize-space()='Sign in']")
    dashboard_header=(By.XPATH, "//h1[normalize-space()='Dashboard']")

     #Action---

    def set_username(self, username):
        self.type(self.Username_txtbox, username)

    def set_password(self,password):
        self.type(self.Password_txtbox,password)

    def click_login(self):
        self.click(self.btn_signin)

    def is_dashboard_displayed(self):
        return self.is_displayed(self.dashboard_header)





















