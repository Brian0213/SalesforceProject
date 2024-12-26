import time

import pytest
import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.LoginPage import LoginPage
from Pages.OpportunityPage import OpportunityPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_SalesOpportunity:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    opportunity = "OLUWASEGUN - DON'T USE THIS."
    party = "Meggitt (rockmart) Inc"
    contact = "Melissa Erickson"
    type = "Service - Commercial"
    subtype = "Repair"

    @pytest.mark.sales
    def test_Opportunity(self, setup):
        self.logger.info("*****Starting The Sales Opportunity Test*****")
        # Call the Browser Configuration
        self.logger.info("*****Call the Browser Configuration*****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        # Open the Website URL
        self.logger.info("*****Open the Website URL*****")
        self.driver.get(self.baseURL)
        # assert self.driver.current_window_handle == self.baseURL, "Failed to open the website URL."
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
        assert "Home | Salesforce" in self.driver.title, "Failed to log in; Home | Salesforce page not displayed."

        self.Op = OpportunityPage(self.driver)
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        print(parentwindowid, childwindowid)
        # Click the Account Tab
        self.logger.info("*****Click the Account Tab*****")
        self.Op.clickAccountTab()
        time.sleep(3)
        # assert "Accounts" in self.driver.title, "Failed to navigate to the Account tab."
        # Click the Account Name
        self.logger.info("*****Click the Account Name*****")
        self.Op.clickAccountName()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 220)")
        time.sleep(5)
        # Click the Location Name
        self.logger.info("*****Click the Location Name*****")
        self.Op.clickLocation()
        # Click the New Opportunity Button
        self.logger.info("*****Click the New Opportunity Button*****")
        self.Op.clickNewOpp()
        time.sleep(5)
        # Switch to the New Opportunity Window
        self.logger.info("*****Switch to the New Opportunity Window*****")
        self.driver.switch_to.window(childwindowid)
        time.sleep(5)
        # assert "Georgia Aquarium For Testing | Salesforce" in self.driver.title, "Failed to switch to the New Opportunity window."
        # Select the Miner Sales Opportunity Record Type
        self.logger.info("*****Select the Miner Sales Opportunity Record Type*****")
        self.Op.clickMinSales()
        time.sleep(8)
        # Click the New Opportunity Window Next Button
        # self.logger.info("*****Click the New Opportunity Window Next Button*****")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
        time.sleep(3)
        # Enter a value in the Opportunity Field
        self.logger.info("*****Enter a value in the Opportunity Field*****")
        self.Op.enterOppName(self.opportunity)
        time.sleep(3)
        # Select Customer Account
        self.logger.info("*****Select Customer Account*****")
        self.Op.selAccount()
        time.sleep(3)
        # # Click the Lookup Field
        # self.Op.lookupAccount11()
        # time.sleep(3)
        # # Fill the Lookup Field with the Desired Selection
        # self.Op.lookupAccount2()
        # time.sleep(3)
        # Select the Paying Party
        self.logger.info("*****Select the Paying Party*****")
        self.Op.payParty()
        # self.Op.payingParty(self.party)
        time.sleep(3)
        # Click the Primary Contact Field
        self.logger.info("*****Click the Primary Contact Field*****")
        self.Op.primaryContact()
        time.sleep(5)
        # Scroll Down to a selection
        self.logger.info("*****Scroll Down to a selection*****")
        self.Op.primaryContact1()
        time.sleep(4)
        # Scroll Down to a selection
        # self.Op.primaryContact3()
        # time.sleep(3)
        # Scroll Down to a selection
        # self.Op.primaryContact4()
        # time.sleep(3)
        # Fill the Primary Contact with the Desired Selection
        self.logger.info("*****Fill the Primary Contact with the Desired Selection*****")
        self.Op.primaryContact2()
        time.sleep(3)
        # Click the Order Type Field
        self.logger.info("*****Click the Order Type Field*****")
        self.Op.orderType()
        time.sleep(3)
        # Select the Order Type Pick
        self.logger.info("*****Select the Order Type Pick*****")
        self.Op.servcomm()
        time.sleep(3)
        # Scroll the Order Sub Field into view
        self.logger.info("*****Scroll the Order Sub Field into view*****")
        self.Op.orderSubScr()
        time.sleep(3)
        # Click the Order Sub Type Field
        self.logger.info("*****Click the Order Sub Type Field*****")
        self.Op.orderSub()
        # self.Op.orderSubType()
        time.sleep(3)
        # Select the Order Sub Type Pick
        self.logger.info("*****Select the Order Sub Type Pick*****")
        self.Op.pickRepair()
        time.sleep(3)
        # Click the Next Button in the New Opportunity Window
        self.logger.info("*****Click the Next Button in the New Opportunity Window*****")
        self.Op.newOppoPageButton()
        time.sleep(5)
        # Click the Opportunity Success Button
        self.logger.info("*****Click the Opportunity Success Button*****")
        self.Op.opportunitySuccess()
        # assert "Opportunity Details" in self.driver.title, "Failed to create the opportunity."
        # print the page web page title
        self.logger.info("*****Print the page web page title*****")
        print(self.driver.title)
        time.sleep(10)
        self.logger.info("*****Sales Opportunity Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/SalesOpportunityPage.png")
        self.logger.info("*****Close the Application and Browser*****")
        self.driver.quit()








        # loc_record = self.(By.XPATH, "//span[normalize-space()='LCR-025151']")





        # self.Op.clickNextBtn()
        #
        # self.driver.switch_to.frame(1)
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//article[@class='slds-is-relative']//flowruntime-navigation-bar[@class='slds-card__footer navigationBar']").click()
        # time.sleep(5)
        # Clicking the Location Record
        #self.driver.switch_to.frame("//flexipage-component2[@data-component-id='flexipage_tabset']//div[@class='slds-tabs_card']")
        #time.sleep(3)