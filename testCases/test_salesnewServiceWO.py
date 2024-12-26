import time

import pytest
import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.LoginPage import LoginPage
from Pages.ServiceWOPage import NewServiceWOPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_ServiceWO:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    woid = "AutoT"
    crw = "3"
    hrs = "6"

    @pytest.mark.sales
    def test_ServiceWO(self, setup):
        self.logger.info("*****Starting The Create New Service Work Order Test*****")
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

        # Define the Service WO Page Driver
        self.Ws = NewServiceWOPage(self.driver)
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        # Click on the Account tab
        self.Ws.clickAccountTab()
        time.sleep(3)
        # Click on an Account Name
        self.Ws.clickAccountName()
        time.sleep(3)
        # Scroll Account Page to view the Location ID
        self.driver.execute_script("window.scrollBy(0, 100)")
        time.sleep(5)
        # Click the Location ID
        self.Ws.clickLocation()
        time.sleep(3)
        # Click the New Service Work Order Button
        self.Ws.serviceWOBtn()
        time.sleep(3)
        # Switch to the Work Order window/form
        self.driver.switch_to.window(childwindowid)
        time.sleep(5)
        # Enter the Work Order Subject
        self.Ws.workOrderSubject(self.woid)
        time.sleep(3)
        # Select a Site Contact
        self.Ws.selectSiteContactNotList()
        time.sleep(3)
        # Select the AP Contact
        self.Ws.selectAPContactNotList()
        time.sleep(3)
        # Scroll to the Desired Site Contact
        self.Ws.siteContact()
        time.sleep(3)
        # Click enter to display the Site Contact in the Site Contact field.
        self.Ws.siteContact3()
        time.sleep(3)
        # Scroll to the Desired AP Contact
        self.Ws.apContact()
        time.sleep(3)
        # Click enter to display the AP Contact in the AP Contact field.
        self.Ws.siteContact3()
        time.sleep(3)
        # Select the Order Type
        self.Ws.orderTypeServ()
        time.sleep(3)
        # Select the Order Sub Type
        self.Ws.subTypeServRP()
        time.sleep(3)
        # Select the Equipment Type
        self.Ws.equipTypeMisc()
        time.sleep(3)
        # Select the Priority
        self.Ws.priorSameDayService()
        time.sleep(3)
        # Select the Labor Source
        self.Ws.labSrcSubcontracted()
        time.sleep(3)
        # Check the Scissor Lift Required? checkbox
        self.Ws.scissLiftReq()
        time.sleep(3)
        # Enter the Crew Size
        self.Ws.crewSize(self.crw)
        time.sleep(3)
        # Enter the Est. Labor Hrs per Crew Member
        self.Ws.estLaborHrs(self.hrs)
        time.sleep(3)
        # Click the Save Button
        self.Ws.clickSave()
        time.sleep(15)
        self.logger.info("*****Create Unquoted Work Order Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/WorkOrderPage.png")
        self.driver.quit()
