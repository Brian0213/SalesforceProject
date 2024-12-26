import time

import pytest
import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.LoginPage import LoginPage
from Pages.OpportunityPage import OpportunityPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_Opportunity:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    opportunity = "MONAUG"
    party = "Meggitt (rockmart) Inc"
    contact = "Melissa Erickson"

    @pytest.mark.pm
    def test_PMOpportunity(self, setup):
        self.logger.info("*****Starting The New Opportunity Test*****")
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
        time.sleep(7)

        self.Op = OpportunityPage(self.driver)
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        print(parentwindowid, childwindowid)
        # Click the Account Tab
        self.Op.clickAccountTab()
        time.sleep(3)
        # Click the Account Name
        self.Op.clickAccountName()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 100)")
        time.sleep(5)
        # Click the Location Name
        self.Op.clickLocationUat()
        # Clicking the New Opportunity Button
        self.Op.clickNewOpp()
        time.sleep(5)
        # Switch to the New Opportunity Window
        self.driver.switch_to.window(childwindowid)
        time.sleep(5)
        # Select the Miner PM Opportunity Record Type
        self.Op.clickMinPM()
        time.sleep(5)
        # Click the New Opportunity Window Next Button
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
        time.sleep(3)
        # Enter a value in the Opportunity Field
        self.Op.enterOppName(self.opportunity)
        time.sleep(3)
        # Select Customer Account
        self.Op.selAccount()
        time.sleep(3)
        # # Fill the Lookup Field with the Desired Selection
        # self.Op.lookupAccount2()
        # Select the Paying Party
        self.Op.payParty()
        #self.Op.payingParty(self.party)
        time.sleep(3)
        # Click the Primary Contact Field
        self.Op.primaryContact()
        time.sleep(5)
        # Scroll Down to a selection
        self.Op.primaryContact1()
        time.sleep(4)
        # Scroll Down to a selection
        # self.Op.primaryContact3()
        # time.sleep(3)
        # Scroll Down to a selection
        # self.Op.primaryContact4()
        # time.sleep(3)
        # Fill the Primary Contact with the Desired Selection
        self.Op.primaryContact2()
        time.sleep(3)
        # Click the Next Button in the New Opportunity Window
        self.Op.newOppoPageButton()
        time.sleep(5)
        # Click the Opportunity Success Button
        self.Op.opportunitySuccess()
        time.sleep(10)
        # Web page title test
        act_title = self.driver.title
        print(act_title)
        # Verifying the page title
        assert "MONAUG" in self.driver.title
        self.logger.info("*****PM Opportunity Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/PMOpportunityPage.png")
        self.driver.quit()
