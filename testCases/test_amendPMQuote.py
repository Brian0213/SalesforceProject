import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.EditQuotePage import EditQuotePage
from Pages.LoginPage import LoginPage
from Pages.ProductFilterPage import ProductFilterPage
from Pages.PartProdLinePage import PartProdLinePage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_AmendSalesQuote:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    @pytest.mark.sales
    def test_AmendSalesQuote(self, setup):
        self.logger.info("*****Starting The Quote -> DocuSign Test*****")
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
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        # childwindowid2 = windowsIDs[2]
        print(parentwindowid, childwindowid)
        self.logger.info("*****Starting The Quote Page Test*****")
        self.qp.clickCpqQuoteTab()
        time.sleep(5)
        self.qp.PMQuote1()
        time.sleep(3)
        self.qp.amendButton()
        # Switch to the Amend Quote Window
        self.driver.switch_to.window(childwindowid)
        time.sleep(3)
        # Select Amend Quote Reason
        self.qp.amendBuChange()
        time.sleep(3)
        # Click the Next Button to Complete the Amendment
        self.qp.amendComplete()
        time.sleep(10)
        self.logger.info("*****Sales Amend Quote Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/AmendPMQuote.png")
        self.driver.quit()