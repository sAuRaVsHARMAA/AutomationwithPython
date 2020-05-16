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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestTabs:
    driver = webdriver.Chrome("C:/Users/Saurav/PycharmProjects/AutomationwithPython/Drivers/chromedriver.exe")
    ut = UtilsData()
    locate = LocatorFirstPage()
    locate_tab = LocatorLoginPage()
    ua = UserAction(driver)
    main_window = None
    action = ActionChains(driver)

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
        self.driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_womentab(self, setup):
        try:
            self.action.move_to_element(self.driver.find_element(By.XPATH, self.locate.women_tab_xpath)). \
                move_to_element(self.driver.find_element(By.XPATH, self.locate.w_tops_xpath)).click().perform()
            t = self.driver.find_element(By.XPATH, "//div[@id='subcategories']//li[1]//div[1]//a[1]").is_displayed()
            b = self.driver.find_element(By.XPATH, "//div[@id='subcategories']//li[2]//div[1]//a[1]//img[1]").is_displayed()
            assert True if t == b else False
            self.driver.find_element(By.XPATH, "//div[@id='subcategories']//li[1]//div[1]//a[1]").send_keys(Keys.CONTROL +
                                                                                                            Keys.RETURN)
            self.driver.find_element(By.XPATH, "//div[@id='subcategories']//li[2]//div[1]//a[1]"). \
                send_keys(Keys.CONTROL + Keys.RETURN)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[2])
            assert self.driver.title == "T-shirts - My Store"
            self.driver.switch_to.window(handles[1])
            assert self.driver.title == "Blouses - My Store"
        except AssertionError as e:
            self.ut.logger("error", "Test Failed... Page title does not match", e)
            name = "Screenshot " + self.ut.whoami() + moment.now().strftime('%d-%b-%Y_%I:%M:%S %p')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)







