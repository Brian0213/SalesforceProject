import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.EditQuotePage import EditQuotePage
from Pages.LoginPage import LoginPage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_PMQuote:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    @pytest.mark.pm
    def test_PMQuotedWO(self, setup):
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
        print(parentwindowid, childwindowid)
        self.logger.info("*****Starting The PM Work Order Create Test*****")
        self.qp.clickCpqQuoteTab()
        time.sleep(5)
        self.qp.PMQuote1()
        time.sleep(2)
        self.qp.clickPMPlantab()
        time.sleep(3)
        self.qp.clickPMPlanId()
        time.sleep(5)
        # Switch to the New Opportunity Window
        # self.driver.switch_to.window(childwindowid)
        # self.driver._switch_to.frame(0)
        # self.qp.details()
        # time.sleep(4)
        # self.qp.clickPen()
        # self.qp.relatedTab()
        # time.sleep(4)
        # # self.driver.switch_to.window(childwindowid)
        # self.driver._switch_to.frame(0)
        # time.sleep(5)
        # self.qp.mainAsset()
        self.qp.genWO()
        time.sleep(8)
        # self.qp.nxtCreate()
        # time.sleep(20)
        self.qp.clickFinish()
        # time.sleep(3)
        # self.qp.clickPMPWOtab()
        # time.sleep(4)
        # self.qp.clickWorkOrderID()
        time.sleep(10)
        self.logger.info("*****Create PM WO from Opportunity Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/PMQuoteWOPage.png")
        self.driver.quit()


