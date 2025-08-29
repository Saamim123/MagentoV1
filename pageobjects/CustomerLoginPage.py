from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage

class CustomerLoginPage(BasePage):
    email_id=(By.ID,"email")
    password_id=(By.ID,"password")
    login_linktext=(By.XPATH,"//fieldset[@class='fieldset login']//span[contains(text(),'Bejelentkezés')]")
    dashboard_myaccount_xpath=(By.XPATH,"//span[@class='base']")

    def set_useremail(self,email):

        self.type(self.email_id,email)

    def set_password(self,password):
        self.type(self.password_id,password)

    def click_login(self):
        self.click(self.login_linktext)

