import account

import pickle
import time

import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CheckOutBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=/home/mike/chrome-checkout")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://www.mediamarkt.de/")
        # self.accept_cookies()

    def accept_cookies(self):
        button = self.driver.find_element_by_id("privacy-layer-accept-all-button")
        button.click()

    def login(self, email, password):

        # if os.path.exists("session.data"):
        #     with open("session.data", "rb") as file:
        #         cookies = pickle.load(file)
        #         print("Session loaded from file")
        #         for cookie in cookies:
        #             print(cookie)
        #             self.driver.add_cookie(cookie)
        #         return True

        self.driver.get("https://www.mediamarkt.de/de/myaccount")
        time.sleep(5)
        email_input = self.driver.find_element_by_id("mms-login-form__email")
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_id("mms-login-form__password")
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element_by_id("mms-login-form__login-button").click()
        time.sleep(3)
        # with open("session.data", "wb") as file:
        #     pickle.dump(self.driver.get_cookies(), file)
        #     for cookie in self.driver.get_cookies():
        #         print(cookie)

    def add_product_to_chart(self, link):
        self.driver.get(link)
        time.sleep(1)
        add_to_cart_button = self.driver.find_element_by_css_selector(
            '[data-test="a2c-Button"]'
        )
        time.sleep(2)

    def checkout(self):
        self.driver.get("https://www.mediamarkt.de/checkout/payment")
        time.sleep(1)
        self.driver.find_elements_by_class_name(
            "SelectGroupstyled__SelectGroupItemContainer-sc-1iooaif-0"
        )[2].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name(
            "ContinueButton__StyledContinue-fh9abp-0"
        )[1].click()

        # this is how you click the final checkout button
        # self.driver.find_elements_by_class_name(
        #     "ContinueButton__StyledContinue-fh9abp-0"
        # )[1].click()

    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    checkout_bot = CheckOutBot()

    # checkout_bot.login(account.email, account.password)
    # time.sleep(30)
    # exit()

    checkout_bot.add_product_to_chart(
        "https://www.mediamarkt.de/de/product/_sandisk-extreme%C2%AE-2484123.html"
    )
    checkout_bot.checkout()
    time.sleep(20)
