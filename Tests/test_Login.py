from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
import allure
import moment
import logging

import sys
sys.path.append("C:/Users/Saurav/PycharmProjects/AutomationwithPython")
from Locators.Locators_First_Page import LocatorFirstPage
from Pages.First_Page import UserAction
from Locators.Locators_LoginPage import LocatorLoginPage
from utils.utils import UtilsData


class TestLogin:
    driver = webdriver.Chrome("C:/Users/Saurav/PycharmProjects/AutomationwithPython/Drivers/chromedriver.exe")
    locate = LocatorFirstPage()
    locate1 = LocatorLoginPage()
    ua = UserAction(driver)
    ut = UtilsData()

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.fixture(scope='session')
    def setup(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(30)
        yield
        self.driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.basic
    def test_login(self, setup):
        try:
            self.driver.get(self.ut.baseurl)
            self.ua.click_generic("xpath", self.locate.sign_in_xpath)
            self.ua.pass_value_generic_func("id",self.locate.sign_in_email_id, self.ut.login_email)
            self.ua.pass_value_generic_func("id", self.locate.sign_in_password_id, self.ut.login_password)
            self.ua.click_generic("id", self.locate.sign_in_button_id)
            acc_name = self.driver.find_element(By.CLASS_NAME, "account").text
            assert acc_name == "Saurav Sharm"
        except AssertionError as e:
            self.ut.logger("error", "Page title does not match" )
            print("Page title are different in Method: " + self.ut.whoami())
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.driver.get_screenshot_as_file("C:/Users/Saurav/PycharmProjects/AutomationwithPython/Screenshots"
                                               "/Screenshot.png") 

    def test_addtocart(self, setup):
        try:
            self.ua.pass_value_generic_func("id", "search_query_top", "shirt")
            self.ua.click_generic("name", self.locate.search_button_name)
            self.ua.click_generic("xpath", "//li[5]//a[1]//img[1]")
            drp = Select(self.driver.find_element(By.ID, "group_1"))
            drp.select_by_visible_text("L")
            self.ua.click_generic("name", "Submit")
            self.ua.click_generic("xpath", "//a[@class='btn btn-default button button-medium']")
            assert self.driver.title == "Order - My Store"
        except AssertionError as e:
            self.ut.logger("error", "Page title does not match" )
            print("Page title are different in Method " + self.ut.whoami())
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)

    def test_payment(self, setup):
        try:
            self.ua.click_generic("xpath", "//*[@id='center_column']/p[2]/a[1]")
            self.ua.click_generic("name", "processAddress")
            self.ua.click_generic("id", "cgv")
            self.ua.click_generic("name", "processCarrier")
            self.ua.click_generic("class_name", "bankwire")
            self.ua.click_generic("xpath", "//*[@id='cart_navigation']/button")
            assert self.driver.title == "Order confirmation - My Store"
            self.ua.click_generic("xpath", "//*[@id='center_column']/p/a")
            assert self.driver.title == "Order history - My Store"
            print("Order Successfully placed ")
        except AssertionError:
            self.ut.logger("error", "Page title does not match" )
            print("Page title are different in Method " + self.ut.whoami())
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)

    @pytest.mark.basic
    def test_signout(self, setup):
        try:
            self.ua.click_generic("class_name", self.locate1.sign_out_classname)
            assert self.driver.title == "Login - My Store"
        except AssertionError:
            self.ut.logger("error", "Page title does not match" )
            print("Page title are different in Method " + self.ut.whoami())
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)






















