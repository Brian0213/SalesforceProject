import time

import pytest
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.OpportunityPage import OpportunityPage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_SalesDescription:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    quotename = "Wembley"
    descrip = "Door Products"

    @pytest.mark.sale2e
    def test_editOpportunityDescription(self, setup):
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
        time.sleep(5)
        self.qp.OppEdit()
        self.driver.switch_to.window(childwindowid)
        time.sleep(5)
        # self.driver.execute_script("window.scrollBy(0, 500)")
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]').send_keys("Noted")
        self.qp.winDescrip(self.descrip)
        # self.driver.execute_script("window.scrollBy(0, 500)")
        # time.sleep(5)
        # self.qp.clickDescripPen()
        # self.driver.find_element(By.XPATH, "//button[@title='Edit Description']").click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//button[@title='Edit Description']").clear()
        time.sleep(5)
        # self.driver.find_element(By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]').send_keys("Noted")
        # self.qp.clnDescrip()
        # self.qp.fillDescrip(self.noted)
        # time.sleep(5)
        self.qp.saveDescriptionEdit()
        # time.sleep(5)
        self.driver.quit()
