import time

import pytest
import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.LoginPage import LoginPage
from Pages.ContactPage import ContactPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_Contact:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    fname = "Arise"
    mname = "Frankfort"
    lname = "Hamburg"
    email = "arise.hamb@input.com"
    phone = "7807650011"
    mobile = "7807650011"
    title = "Security Lead"
    addy = "780 Technology Street"

    @pytest.mark.sales
    def test_Contact(self, setup):
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

        self.Cp = ContactPage(self.driver)
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        print(parentwindowid, childwindowid)
        # Click on Accounts Tab
        self.Cp.clickAccountTab()
        time.sleep(3)
        # Click the Account Name
        self.Cp.clickAccountName()
        time.sleep(3)
        # Click the Add Contact Button
        self.Cp.clickContactBtn()
        time.sleep(3)
        # Select the Create New Radio Button
        self.Cp.clickCreateNewContact()
        time.sleep(3)
        # Enter the Salutation dropdown
        self.Cp.Salutation()
        time.sleep(2)
        # Select a Salutation
        self.Cp.pickDr()
        time.sleep(2)
        # Enter the First Name
        self.Cp.firstName(self.fname)
        time.sleep(2)
        # Enter the Middle Name
        self.Cp.middleName(self.mname)
        time.sleep(2)
        # Enter the Last Name
        self.Cp.lastName(self.lname)
        time.sleep(2)
        # Enter the Email
        self.Cp.eMail(self.email)
        time.sleep(2)
        # Enter the Phone Number
        self.Cp.pHone(self.phone)
        time.sleep(2)
        # Enter the Mobile Number
        self.Cp.mobilePhone(self.mobile)
        time.sleep(2)
        # Enter the Contact's Title
        self.Cp.tiTle(self.title)
        time.sleep(3)
        # Click the Next Button
        self.Cp.clickNext()
        time.sleep(3)
        # Switch to the Add Contact Window
        self.driver.switch_to.window(childwindowid)
        time.sleep(3)
        # Select a Role
        self.Cp.purchaseManager()
        time.sleep(3)
        # Move the Role to the Chosen field
        self.Cp.Next()
        time.sleep(5)
        # Click the Add Contact Window's Next Button
        self.Cp.clickNext2()
        time.sleep(3)
        # Click the Contact Creation Complete Button
        self.Cp.confirmContact()
        time.sleep(10)
        self.logger.info("*****Create Contact Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/CreateContactPage.png")
        self.driver.quit()








