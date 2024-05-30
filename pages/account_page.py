import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class AccountPage(BasePage):
    PAGE_URL = "https://magento.softwaretestingboard.com/"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "(//a[text() = 'Create an Account'][1])")
    FIRST_NAME = (By.XPATH, "//*[@id='firstname']")
    LAST_NAME = (By.XPATH, "//input[@title='Last Name']")
    EMAIL = (By.XPATH, "//input[@title='Email']")
    PASSWORD = (By.XPATH, "//input[@title='Password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@title='Confirm Password']")
    CREATE_BUTTON = (By.XPATH, "//button[@class='action submit primary']")

    def create_an_account_with_valid_data(self, driver):
        first_name = "IVAN"
        last_name = "IVANOV"
        email = "IVAN@TEST.COM"
        password = "Qwerty123"
        self.element_is_visible(AccountPage.CREATE_ACCOUNT_BUTTON).click()
        self.element_is_visible(AccountPage.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(AccountPage.LAST_NAME).send_keys(last_name)
        self.element_is_visible(AccountPage.EMAIL).send_keys(email)
        self.element_is_visible(AccountPage.PASSWORD).send_keys(password)
        self.element_is_visible(AccountPage.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_clickable(AccountPage.CREATE_BUTTON).click()
        time.sleep(4)

