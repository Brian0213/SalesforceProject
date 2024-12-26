import time

import pytest
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.OpportunityPage import OpportunityPage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_CreateQuote:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    quotename = "OLU: QTP"
    infor = "MHE"

    @pytest.mark.pm
    def test_createPMQuote(self, setup):
        self.logger.info("*****Starting The Create PM Quote From Opportunity Test*****")
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

        # Define the Quote Page Driver
        self.qp = QuotePage(self.driver)
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        print(parentwindowid, childwindowid)
        # Click the Opportunity Tab
        self.qp.clickOpportunityTab()
        time.sleep(3)
        # Click on an Opportunity ID
        self.qp.clickOpportunityIDPM()
        time.sleep(3)
        # Click on the New CPQ Quote Button
        self.qp.clickNewQuoteBtn()
        time.sleep(5)
        # Switch to the New CPQ Quote Window
        self.driver.switch_to.window(childwindowid)
        time.sleep(4)
        # Fill the Quote Name field
        self.qp.setQuoteName(self.quotename)
        time.sleep(4)
        # Fill the Quote Description field
        self.qp.quoteDescription(self.infor)
        time.sleep(4)
        # Click the Save Button
        self.qp.clickSave()
        time.sleep(10)
        # Web page title test
        act_title = self.driver.title
        print(act_title)
        # Verifying the page title
        # assert "Victoria Island" in self.driver.title
        self.logger.info("*****Create PM Quote from Opportunity Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/PMQuoteCreatedPage.png")
        self.driver.quit()
