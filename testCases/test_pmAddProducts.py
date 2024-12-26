import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.EditQuotePage import EditQuotePage
from Pages.LoginPage import LoginPage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_PMAddProducts:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    searchitem = "PM1009"
    searchitem2 = "PM1024"
    searchitem3 = "PM1039"

    @pytest.mark.pme2e
    def test_PMAddProd(self, setup):
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
        time.sleep(2)
        # Click the Edit Lines Button
        self.qp.clickEditlines()
        time.sleep(7)
        # Switch to Frame
        self.driver.switch_to.frame(0)

        self.logger.info("*****Starting The Quote Line Editor Test*****")
        self.eqp = EditQuotePage(self.driver)
        # Click the Add Product Button
        self.eqp.AddProdButton()
        time.sleep(3)
        # Search for Product
        self.eqp.SearchProduct(self.searchitem)
        time.sleep(3)
        # Click the Search Button
        self.eqp.SearchButton()
        time.sleep(3)
        # Click the Apply Button
        self.eqp.ApplyButton()
        time.sleep(3)
        # Click the Product Checkbox
        self.eqp.ProductCheckbox()
        time.sleep(3)
        # Click the Select Button
        self.eqp.SelectButton()
        time.sleep(3)
        # Click the Add Product Button
        self.eqp.AddProdButton()
        time.sleep(3)
        # Search for Product 2
        self.eqp.SearchProduct(self.searchitem2)
        time.sleep(3)
        # Click the Search Button
        self.eqp.SearchButton()
        time.sleep(3)
        # Click the Product Checkbox
        self.eqp.ProductCheckbox()
        time.sleep(3)
        # Click the Select Button
        self.eqp.SelectButton()
        time.sleep(2)
        # Click the Add Product Button
        self.eqp.AddProdButton()
        time.sleep(3)
        # Search for Product 3
        self.eqp.SearchProduct(self.searchitem3)
        time.sleep(3)
        # Click the Search Button
        self.eqp.SearchButton()
        time.sleep(5)
        # Click the Product Checkbox
        self.eqp.ProductCheckbox()
        time.sleep(2)
        # Click the Select Button
        self.eqp.SelectButton()
        time.sleep(5)
        # Click the Save Button
        self.eqp.SaveButton()
        time.sleep(5)
        # # Click the Submit For Approval Button
        # self.qp.clickSubFApproval()
        # time.sleep(5)
        # # Click the Generate Quote Button
        # self.qp.clickGenOHQuote()
        # time.sleep(15)
        # # Switch Frame
        # self.driver.switch_to.frame(0)
        # time.sleep(10)
        # #print(name)
        # # Click the Send For Button
        # self.qp.SendFSigna()
        # time.sleep(20)
        # # Click the Next Button
        # self.qp.DocuSNext()
        # time.sleep(20)
        # # Click the Next Button
        # self.qp.DocuSNext()
        # time.sleep(20)
        # # Click the Customer Send Button
        # self.qp.CustomerSend()
        # time.sleep(20)
        self.logger.info("*****PM Quote Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/PMQuotepage.png")
        self.driver.quit()

