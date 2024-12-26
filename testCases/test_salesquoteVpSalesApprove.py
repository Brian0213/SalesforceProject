import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.LoginPage import LoginPage
from Pages.QuotePage import QuotePage
from Pages.CreateWorkOrderPage import CreateWorkOrderPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_QuoteVPSales:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()
    note = "Manager Approved"
    note2 = "VP of Sales Approved"

    @pytest.mark.approval
    def test_VPofSalesApproval(self, setup):
        self.logger.info("*****Starting The VP of Sales Approval Test*****")
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
        self.qp.clickCpqQuoteTab()
        time.sleep(5)
        self.qp.clickQuote()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 2230)")
        time.sleep(5)
        self.qp.ApprovallinkVP()
        time.sleep(5)
        self.qp.ApprovalBtn()
        time.sleep(5)
        self.driver.switch_to.frame(1)
        time.sleep(5)
        self.qp.EnterApproveNote(self.note2)
        time.sleep(3)
        self.qp.ApproveComplete()
        time.sleep(10)
        self.logger.info("*****Vp of Sales Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/VPofSalesApprovalPage.png")
        self.driver.quit()
