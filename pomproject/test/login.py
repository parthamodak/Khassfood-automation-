from selenium import webdriver
#from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#import time
import unittest
#from pomproject.pages.LoginPage import LoginPage
from pomproject.pages.home import AllNav

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        serv_obj = Service(executable_path="C:/Users/mmpar/OneDrive/Desktop/New folder/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)

        cls.driver.maximize_window()

    @classmethod
    def test_login_valid(self):

        driver = self.driver
        driver.get("https://www.khaasfood.com/")
        #nav=AllNav(driver)

        #nav.top_navbar_check()
        #nav.secound_navbar_check()


        login = LoginPage(driver)
        login.login_regerter()
        login.enter_usename("mmodak642@gmail.com")
        # login.enter_password("53pMM80@")
        # login.login_enter()
        # self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div[3]/div[2]/a").click()
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("mmodak642@gmail.com")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("53pMM80@")
        # self.driver.find_element(By.XPATH,"//button[@class='btn btn-color-primary btn-shape-semi-round btn-size-default btn-full-width'][normalize-space()='Login']").click()
        #self.time.sleep(2)


