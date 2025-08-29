from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage
from pageobjects.Luma_Homepage import Luma_homepage

class Myaccountpage(BasePage):

    logout_dropdown_xpath=(By.XPATH,"//span[@class='customer-name active']//button[@type='button']")
    logout_linktext=(By.LINK_TEXT, "Sign Out")
    myaccount_confirmation_xpath=(By.XPATH,"//span[@class='base']")
    Bags_link_xpath=(By.XPATH,"//span[normalize-space()='Bags']")
    wish_icon_xpath=(By.XPATH,"//a[@title='Add to Wish List']")
    remove_from_wish_list=(By.XPATH,"//a[@title='Remove This Item']")
    removal_cnf_msg=(By.XPATH,"//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    wish_cnf_msg=(By.XPATH,"//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    def click_dropdown(self):

        self.click(self.logout_dropdown_xpath)

    def click_logout(self):
        self.click(self.logout_linktext)

    def capture_myaccount_cnf(self):
        self.get_text(self.removal_cnf_msg)

    def click_bag(self):
        self.click(self.Bags_link_xpath)

    def click_wish_icon(self):
        self.click(self.wish_icon_xpath)

    def wishlist_cnf_msg(self):
        return self.get_text(self.wish_cnf_msg)

    def remove_item_from_wish_list(self):
        self.click(self.wish_icon_xpath)

    def capture_removal_from_wish_msg(self):
        return self.is_displayed(self.removal_cnf_msg)








