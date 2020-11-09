import account

import time

print(account.email)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CheckOutBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.mediamarkt.de/")
        self.accept_cookies()

    def accept_cookies(self):
        button = self.driver.find_element_by_id("privacy-layer-accept-all-button")
        button.click()

    def login(self, email, password):

        self.driver.get("https://www.mediamarkt.de/de/myaccount")
        time.sleep(5)
        email_input = self.driver.find_element_by_id("mms-login-form__email")
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_id("mms-login-form__password")
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element_by_id("mms-login-form__login-button").click()

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
        # )[2].click()

    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    checkout_bot = CheckOutBot()

    checkout_bot.login(account.email, account.password)
    checkout_bot.add_product_to_chart(
        "https://www.mediamarkt.de/de/product/_sandisk-extreme%C2%AE-2484123.html"
    )
    checkout_bot.checkout()
    time.sleep(20)
