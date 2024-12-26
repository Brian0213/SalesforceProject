import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.EditQuotePage import EditQuotePage
from Pages.LoginPage import LoginPage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_PMDocuSign:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    @pytest.mark.pme2e
    def test_PMDocuSign(self, setup):
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
        # Click on Signin Button
        self.logger.info("*****Click the Signin Button*****")
        self.lp.clickSignin()
        time.sleep(5)

        self.qp = QuotePage(self.driver)
        self.logger.info("*****Starting The Quote Page Test*****")
        # Click the CPQ Quote Tab
        self.qp.clickCpqQuoteTab()
        time.sleep(5)
        # Click the PM Quote
        self.qp.PMQuote1()
        time.sleep(5)

        self.logger.info("*****Starting The Quote Line Editor Test*****")
        self.eqp = EditQuotePage(self.driver)
        # Click the Submit For Approval Button
        self.qp.clickSubFApproval()
        time.sleep(5)
        # Click the Generate Quote Button
        self.qp.clickGenQuote()
        time.sleep(15)
        # Switch Frame
        self.driver.switch_to.frame(0)
        time.sleep(10)
        #print(name)
        # Click the Send For Button
        self.qp.SendFSigna()
        time.sleep(20)
        # Click the Next Button
        self.qp.DocuSNext()
        time.sleep(20)
        # Click the Next Button
        self.qp.DocuSNext()
        time.sleep(20)
        # Click the Customer Send Button
        self.qp.CustomerSend()
        time.sleep(20)
        self.logger.info("*****PM DocuSign Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/PMDocuSignpage.png")
        self.driver.quit()

