import configparser
import os


config_path = os.path.abspath(os.curdir) + "\\configuration\\config.ini"

config=configparser.RawConfigParser()

config.read(config_path)

class Readconfig:
    @staticmethod
    def get_admin_login_url():
        admin_url=config.get('common info','admin_login_url')
        return admin_url

    @staticmethod
    def admin_email():
        adminemail= config.get('common info', 'admin_email')
        return adminemail

    @staticmethod
    def admin_pwd():
        adminpswd=config.get('common info','admin_password')
        return adminpswd

    @staticmethod
    def get_user_login_url():
        user_login_url=config.get('common info','user_login_url')
        return user_login_url

    @staticmethod
    def get_fname():
        first_name=config.get('common info','fname')
        return first_name

    @staticmethod
    def get_lname():
        last_name = config.get('common info', 'lname')
        return last_name

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_user_login_email():
        email = config.get('common info', 'user_login_email')
        return email

    @staticmethod
    def get_user_login_password():
        password = config.get('common info', 'user_login_password')
        return password

    @staticmethod
    def get_user_login_cnf_msg():
        msg = config.get('common info', 'user_login_confirmation_msg')
        return msg

    @staticmethod
    def get_search_item_name():
        item_name=config.get('common info', 'search_item')
        return item_name

