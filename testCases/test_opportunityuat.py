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
    opportunity = "Old Trafford"
    date = "3/21/2024"
    account = "Encore Wire"
    accountuat = "Aquatherm"
    party = "Miner"
    contact = "Melissa Erickson"
    type = "Service - Commercial"
    subtype = "Repair"

    #loc_record = self.(By.XPATH, "//span[normalize-space()='LCR-025151']")

    def test_Opportunity(self, setup):
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


        # Define OpportunityPage Driver
        self.Op = OpportunityPage(self.driver)
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        # childwindowid2 = windowsIDs[2]
        print(parentwindowid, childwindowid)
        # Clicking the Account Tab
        self.Op.clickAccountTab()
        time.sleep(3)
        # Clicking the Account Name
        self.Op.clickAccountNameUat()
        time.sleep(3)
        # Clicking the Location Record
        #self.driver.switch_to.frame("//flexipage-component2[@data-component-id='flexipage_tabset']//div[@class='slds-tabs_card']")
        #time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 100)")
        time.sleep(5)
        # self.Op.clickLocRecord()
        # time.sleep(10)
        # Clicking the Location Name
        self.Op.clickLocationUat()
        # Clicking the New Opportunity Icon
        # self.Op.clickLocIcon()
        # Clicking the New Opportunity Button
        self.Op.clickNewOpp()
        # time.sleep(5)
        # Switching to the New Opportunity Window
        self.driver.switch_to.window(childwindowid)
        time.sleep(5)
        # Selecting Miner Sales Opportunity Record Type
        self.Op.clickMinSales()
        # time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
        # self.Op.clickNextBtn()
        # # Clicking the New Opportunity Window Next Button
        # self.driver.switch_to.frame(1)
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//article[@class='slds-is-relative']//flowruntime-navigation-bar[@class='slds-card__footer navigationBar']").click()
        # time.sleep(5)
        time.sleep(3)
        self.Op.enterOppName(self.opportunity)
        time.sleep(3)
        # self.Op.enterClosedate(self.date)
        # time.sleep(3)
        self.Op.lookupAccountUat1()
        time.sleep(3)
        self.Op.lookupAccount2()
        # self.Op.lookAcct()
        # time.sleep(3)
        self.Op.lookupAccount3()
        # self.select = Select(self.driver.find_element((By.XPATH, '//input[@class="slds-combobox__input slds-input"]')))
        # time.sleep(3)
        #self.options = self.select_object.options
        time.sleep(3)
        #self.select_object.select_by_index(1)
        # self.select_by_visible_text("Miner")
        # time.sleep(3)
        # self.Op.pickMiner()
        # self.Op.payingParty(self.party)
        # time.sleep(3)
        # # self.driver.execute_script("window.scrollBy(0, 200)")
        # # time.sleep(5)
        # self.Op.primaryContact(self.contact)
        # time.sleep(5)
        # self.Op.orderType()
        # time.sleep(5)
        # self.Op.servcomm()
        # time.sleep(5)
        # self.Op.orderSubType()
        # time.sleep(5)
        # self.Op.pickInstallation()
        # time.sleep(5)
        # self.Op.newOppoPageButton()
        time.sleep(10)












