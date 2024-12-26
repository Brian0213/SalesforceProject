import time

import pytest
import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.LoginPage import LoginPage
from Pages.ServiceCoordinatorPage import ServiceCoordinatorPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_SCWorkOrder:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    def test_ServiceCoordWO(self, setup):
        self.logger.info("*****Starting The Contact Creation Test*****")
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

        self.Sp = ServiceCoordinatorPage(self.driver)
        self.Sp.clickWaffle()
        time.sleep(5)
        self.Sp.srhMinerService()
        time.sleep(5)
        self.Sp.reMiner()
        time.sleep(3)
        self.Sp.lkServiceCoord()
        time.sleep(3)
        self.Sp.clickServiceCoord()
        # time.sleep(3)
        # self.Sp.userDetailBtn()
        # time.sleep(3)
        # self.driver.switch_to.frame(0)
        # time.sleep(5)
        # self.Sp.clickSCLogBtn()
        # time.sleep(3)
        # self.Sp.clickMenuNav()
        # time.sleep(3)
        # self.Sp.pickWorkOrders()
        # time.sleep(3)
        # self.Sp.newServiceWO()
        # time.sleep(3)
        # self.driver.switch_to.frame(0)
        # time.sleep(5)
        # self.Sp.customerAcct()
        time.sleep(10)
        # self.logger.info("*****Service Coordinator Work Order Test Completed*****")
        # self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/ServiceCoordWO.png")
        # self.driver.quit()


