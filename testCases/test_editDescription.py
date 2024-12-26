import time

import pytest
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.OpportunityPage import OpportunityPage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_DecriptionField:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    fill = "Labor Products"

    @pytest.mark.sales
    def test_DescriptionField(self, setup):
        self.logger.info("*****Starting The Create Sales Quote From Opportunity Test*****")
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
        self.qp.clickOpportunityIDSales()
        time.sleep(3)
        # Click the Edit Button on the Opportunity Page.
        self.qp.clickEditBtn()
        time.sleep(3)
        # Switch into the Edit Window
        self.driver.switch_to.window(childwindowid)
        time.sleep(5)
        # Enter Text or Value into the Description Field
        self.qp.description(self.fill)
        time.sleep(3)
        # Click the Save Edit button to complete the action.
        self.qp.saveDescrip()
        time.sleep(10)
        self.logger.info("*****Edit Opportunity Description Field Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/DescriptionFieldPage.png")
        self.driver.quit()