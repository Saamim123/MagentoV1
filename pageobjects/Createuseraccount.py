import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class create_new_account:

    firstname_input_ID = "firstname"
    lastname_input_ID = "lastname"
    newsletter_checkbox_ID = "is_subscribed"
    checkbox_remoteshopping_ID = "assistance_allowed_checkbox"
    emailbox_ID = "email_address"
    passwordbox_ID = "password"
    cnf_password_ID = "password-confirmation"
    createaccount_Btn_CSS = "form[id='form-validate'] div[class='primary'] span"
    account_creation_cnf_text_xpath = "//div[contains(text(),'Thank you')]"



    def __init__(self, driver):
        self.driver = driver


    def enter_fname(self, fname):
        firstname_field = self.driver.find_element(By.ID, self.firstname_input_ID)
        firstname_field.send_keys(fname)

    def enter_lname(self, lname):
        lastname_field = self.driver.find_element(By.ID, self.lastname_input_ID)
        lastname_field.send_keys(lname)



    def checkbox_newsletter(self):
        newsletter_box = self.driver.find_element(By.ID, self.newsletter_checkbox_ID)
        newsletter_box.click()

    def checkbox_remoteshopping(self):
        remoteshopping_box = self.driver.find_element(By.ID, self.checkbox_remoteshopping_ID)
        remoteshopping_box.click()

    def set_email(self, email):
        enter_email = self.driver.find_element(By.ID, self.emailbox_ID)
        enter_email.send_keys(email)

    def set_password(self, password):
        enter_password = self.driver.find_element(By.ID, self.passwordbox_ID)
        enter_password.send_keys(password)

    def confirm_password(self, password):
        confirm_password = self.driver.find_element(By.ID, self.cnf_password_ID)
        confirm_password.send_keys(password)

    def create_account(self):
        wait = WebDriverWait(self.driver, 10)

        # Wait for button to be clickable
        create_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.createaccount_Btn_CSS))
        )
        create_btn.click()

    def capture_cnf_text(self):
        cnf_text_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.account_creation_cnf_text_xpath))
        )
        return cnf_text_msg.text.strip()
