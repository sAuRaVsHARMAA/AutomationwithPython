import sys
sys.path.append("C:/Users/Saurav/PycharmProjects/AutomationwithPython")
from Locators.Locators_LoginPage import LocatorLoginPage
from Locators.Locators_First_Page import LocatorFirstPage
from Pages.First_Page import UserAction
from utils.utils import UtilsData
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import moment
import time
from selenium.common.exceptions import *
import allure


class TestTabs:
    driver = webdriver.Chrome("C:/Users/Saurav/PycharmProjects/AutomationwithPython/Drivers/chromedriver.exe")
    ut = UtilsData()
    locate = LocatorFirstPage()
    locate_tab = LocatorLoginPage()
    ua = UserAction(driver)

    @pytest.fixture(scope='session')
    def setup(self):
        self.driver.get(self.ut.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(30)
        self.ua.click_generic("xpath", self.locate.sign_in_xpath)
        self.ua.pass_value_generic_func("id", self.locate.sign_in_email_id, self.ut.login_email)
        self.ua.pass_value_generic_func("id", self.locate.sign_in_password_id, self.ut.login_password)
        self.ua.click_generic("id", self.locate.sign_in_button_id)
        yield
        self.driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_history(self, setup):
        try:
            self.ua.click_generic("xpath", self.locate_tab.order_history_tab_xpath)
            assert self.driver.title == "Order history - My Stor"
            self.driver.back()
        except AssertionError as e:
            self.ut.logger("error", "Test Failed... Page title does not match", e)
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime('%d-%b-%Y_%I:%M:%S %p')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.driver.back()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_mycreditslip(self, setup):
        try:
            self.ua.click_generic("xpath", self.locate_tab.my_credit_slip_xpath)
            assert self.driver.title == "Order slip - My Store"
            self.driver.back()
        except AssertionError as e:
            self.ut.logger("error", "Test Failed... Page title does not match", e)
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime('%d-%b-%Y_%I:%M:%S %p')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.driver.back()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_myaddress(self, setup):
        try:
            self.ua.click_generic("xpath", self.locate_tab.my_address_xpath)
            assert self.driver.title == "Addresses - My Store"
            self.driver.back()
        except AssertionError as e:
            self.ut.logger("error", "Test Failed... Page title does not match", e)
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime('%d-%b-%Y_%I:%M:%S %p')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.driver.back()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_my_personal_info(self, setup):
        try:
            self.ua.click_generic("xpath", self.locate_tab.my_personal_info_xpath)
            assert self.driver.title == 'Identity - My Store'
            self.driver.back()
        except AssertionError as e:
            self.ut.logger("error", "Test Failed... Page title does not match", e)
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime('%d-%b-%Y_%I:%M:%S %p')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.driver.back()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_mywishlist(self, setup):
        try:
            self.ua.click_generic("xpath", self.locate_tab.my_wishlist_xpath)
            assert self.driver.title == 'My Stor'
            self.driver.back()
        except AssertionError as e:
            self.ut.logger("error", "Test Failed... Page title does not match", e)
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime('%d-%b-%Y_%I:%M:%S %p')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.driver.back()


