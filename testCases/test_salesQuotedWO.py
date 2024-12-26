import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.LoginPage import LoginPage
from Pages.QuotePage import QuotePage
from Pages.CreateWorkOrderPage import CreateWorkOrderPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_CreateWork:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    @pytest.mark.sales
    def test_CreateWO(self, setup):
        self.logger.info("*****Starting The Create Quote Work Order Test*****")
        # Call the Browser Configuration
        self.logger.info("*****Call the Browser Configuration*****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        # Open the Website URL
        self.logger.info("*****Open the Website URL*****")
        self.driver.get(self.baseURL)
        # Fit the browser screen
        self.logger.info("*****Fit the browser screen*****")
        self.driver.maximize_window()
        # Define LoginPage Driver
        self.logger.info("*****Define LoginPage Driver*****")
        self.lp = LoginPage(self.driver)
        # Fill the UserName field
        self.logger.info("*****Fill the UserName field*****")
        self.lp.setUserName(self.username)
        # Fill the Password field
        self.logger.info("*****Fill the Password field*****")
        self.lp.setPassword(self.password)
        # Click on the Signin Button
        self.logger.info("*****Click the Signin Button*****")
        self.lp.clickSignin()
        time.sleep(5)

        self.qp = QuotePage(self.driver)
        self.logger.info("*****Starting The Create Work Order Test*****")
        time.sleep(3)
        self.logger.info("*****CPQ Quotes Tab Click*****")
        self.qp.clickCpqQuoteTab()
        time.sleep(3)
        self.logger.info("*****CPQ Id Clicked*****")
        self.qp.SalesQuote1()
        time.sleep(5)
        self.qp.clickCreateWO()
        time.sleep(10)

        self.wo = CreateWorkOrderPage(self.driver)
        self.logger.info("*****Finish Button Clicked*****")
        # self.wo.clickFinishBtn()
        # time.sleep(10)
        self.logger.info("*****Scroll to View Work Order Number*****")
        self.driver.execute_script("window.scrollBy(0, 200)")
        # time.sleep(5)
        # self.logger.info("*****Work Order Hyperlink Clicked*****")
        self.wo.clickWorkOrderLk()  # This is not static but dynamic i.e., it changes for each quote.
        time.sleep(5)
        # self.logger.info("*****Work Order Id Clicked*****")
        # self.wo.WorkOID()
        # time.sleep(5)
        self.logger.info("*****Manage Work Orders Tab Clicked*****")
        self.wo.ManWorkDetails()
        time.sleep(10)
        self.logger.info("*****Create Work Order Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/CreateWO.png")
        self.driver.quit()



