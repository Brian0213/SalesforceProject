import time

import pytest
import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.LoginPage import LoginPage
from Pages.LocationPage import LocationPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_Location:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    locationID = "Auto_New"
    address_name = "340 Main Ave, Norwalk, CT 06851, USA"

    @pytest.mark.sales
    def test_Location(self, setup):
        self.logger.info("*****Starting The Add Location Test*****")
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

        self.Pl = LocationPage(self.driver)
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        # childwindowid2 = windowsIDs[2]
        print(parentwindowid, childwindowid)
        # Clicking the Account Tab
        self.Pl.clickAccountTab()
        time.sleep(3)
        self.Pl.clickAccountName()
        time.sleep(3)
        self.Pl.clickaddLocBtn()
        time.sleep(3)
        self.driver.switch_to.window(childwindowid)
        time.sleep(3)
        self.Pl.locationName(self.locationID)
        time.sleep(3)
        self.Pl.relationTypeGC()
        time.sleep(3)
        self.Pl.address(self.address_name)
        time.sleep(3)
        # self.Pl.address4()
        # self.Pl.address4()
        # self.Pl.address22()
        time.sleep(4)
        # self.Pl.primaryP()
        # self.Pl.address23()
        # time.sleep(3)
        # self.Pl.address4()
        # time.sleep(5)
        # self.Pl.address4()
        # # self.Pl.address22()
        # time.sleep(5)
        self.Pl.address3()
        # self.Pl.contactNameScr()
        # time.sleep(3)
        # self.Pl.contactName()
        # time.sleep(3)
        self.Pl.contactName1()
        time.sleep(3)
        self.Pl.contactName2()
        time.sleep(2)
        self.Pl.contactRelationshipPRM()
        time.sleep(3)
        self.Pl.locationSuccess()
        time.sleep(10)
        self.driver.quit()











        # self.Pl.relationshipType()
        # time.sleep(3)
        # self.Pl.relationshipType1()
        # time.sleep(3)
        # self.Pl.relationshipType1()
        # time.sleep(3)
        # self.Pl.relationshipType1()
        # self.Pl.relationshipType2()
        # self.Pl.addressType()
        # # time.sleep(3)
        # self.Pl.addressType1()
        # time.sleep(3)
        # self.Pl.addressType2()
        # time.sleep(3)
        #
        # time.sleep(5)
        # self.Pl.address1()
        # time.sleep(3)
        # self.Pl.address2()
        # self.Pl.address3()
        # time.sleep(5)
        # self.Pl.address3()
        # self.Pl.contactNameScr()
        # time.sleep(5)
        # self.Pl.contactName()
        # time.sleep(3)
        # self.Pl.contactName1()
        # time.sleep(2)
        # self.Pl.contactName1()
        # time.sleep(2)
        # self.Pl.contactName1()
        # time.sleep(2)
        # self.Pl.contactName1()
        # time.sleep(2)
        # self.Pl.contactName2()
        # time.sleep(2)
        # self.Pl.contactRelationshipPRM()
        # time.sleep(2)
        # self.Pl.contactRelationship2()








