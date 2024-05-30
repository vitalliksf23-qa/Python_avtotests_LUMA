import time
from pages.account_page import AccountPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import pytest


class TestCreateAccount:
    def test(self, driver):
        account_page = AccountPage(driver, "https://magento.softwaretestingboard.com/")
        account_page.open()
        account_page.create_an_account_with_valid_data(driver)
