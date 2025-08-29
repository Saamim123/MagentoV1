import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.BasePage import BasePage

class CreateNewAccount(BasePage):

    firstname_input_ID = (By.ID,"firstname")
    lastname_input_ID = (By.ID,"lastname")
    newsletter_checkbox_xpath = (By.XPATH,"//input[@id='is_subscribed']")
    checkbox_remoteshopping_ID = (By.ID, "assistance_allowed_checkbox")
    emailbox_ID = (By.ID, "email_address")
    passwordbox_ID = (By.ID,"password")
    cnf_password_ID = (By.ID,"password-confirmation")
    createaccount_Btn_CSS =(By.CSS_SELECTOR,"form[id='form-validate'] div[class='primary'] span")
    account_creation_cnf_text_xpath = (By.XPATH,"//div[contains(text(),'Thank you')]")


    def enter_fname(self, fname):
        self.type(self.firstname_input_ID,fname)

    def enter_lname(self, lname):
        self.type(self.lastname_input_ID,lname)

    def checkbox_newsletter(self):
        self.click(self.newsletter_checkbox_xpath)

    def checkbox_remoteshopping(self):
        self.click(self.checkbox_remoteshopping_ID)

    def set_email(self, email):
        self.type(self.emailbox_ID,email)

    def set_password(self, password):
        self.type(self.passwordbox_ID,password)

    def confirm_password(self, password):
        self.type(self.cnf_password_ID,password)

    def create_account(self):
        self.click(self.createaccount_Btn_CSS)

    def capture_cnf_text(self):
        return self.get_text(self.account_creation_cnf_text_xpath)