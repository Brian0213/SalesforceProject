import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.LoginPage import LoginPage
from Pages.DiscountPage import DiscountPage
from Pages.ProductFilterPage import ProductFilterPage
from Pages.PartProdLinePage import PartProdLinePage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_SalesQuote:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    # searchitem = "M202-1169"
    # searchitem2 = "M101-1148"
    # searchitem3 = "M202-1491"
    searchitem = "M202-1050"
    searchitem2 = "M202-1801"
    searchitem3 = "M105-1216"
    field = "20"

    @pytest.mark.sales
    def test_Quote(self, setup):
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
        self.logger.info("*****Starting The Quote Page Test*****")
        self.logger.info("*****Click The Quote Tab*****")
        self.qp.clickCpqQuoteTab()
        time.sleep(5)
        self.logger.info("*****Click The Sales Quote*****")
        self.qp.SalesQuote1()
        time.sleep(4)
        self.logger.info("*****Click the Edit Lines Button*****")
        self.qp.clickEditlines()
        time.sleep(7)

        self.dp = DiscountPage(self.driver)
        self.dp.addTwit(self.field)
        time.sleep(10)
        self.logger.info("*****Sales Quote Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/SalesQuotepage.png")
        self.driver.quit()
