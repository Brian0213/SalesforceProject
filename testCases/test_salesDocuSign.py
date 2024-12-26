import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.EditQuotePage import EditQuotePage
from Pages.LoginPage import LoginPage
from Pages.ProductFilterPage import ProductFilterPage
from Pages.PartProdLinePage import PartProdLinePage
from Pages.QuotePage import QuotePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_SalesDocuSign:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    @pytest.mark.sale2e
    def test_SalesDocuSign(self, setup):
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
        time.sleep(5)
        # self.logger.info("*****Click the Edit Lines Button*****")
        # self.qp.clickEditlines()
        # time.sleep(7)
        # self.logger.info("*****Switch to The Quote Line Editor*****")
        # self.driver.switch_to.frame(0)

        self.logger.info("*****Starting The Quote Line Editor Test*****")
        self.eqp = EditQuotePage(self.driver)
        # self.logger.info("*****Click The Add Products Button *****")
        # self.eqp.AddProdButton()
        # time.sleep(3)
        # self.logger.info("*****Lookup a Sales Product*****")
        # self.eqp.SearchField(self.searchitem)
        # time.sleep(3)
        # self.logger.info("*****Search the Sales Product*****")
        # self.eqp.SearchButton()
        # time.sleep(3)
        # self.logger.info("*****Click The Apply Button*****")
        # self.eqp.ApplyButton()
        # time.sleep(3)
        # self.logger.info("*****Click the Product Checkbox*****")
        # self.eqp.ProductCheckbox()
        # time.sleep(3)
        # self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        # self.eqp.SelectButton()
        # time.sleep(3)
        # self.logger.info("*****Click The Add Products Button *****")
        # self.eqp.AddProdButton()
        # time.sleep(3)
        # self.logger.info("*****Lookup a Sales Product*****")
        # self.eqp.SearchField(self.searchitem2)
        # time.sleep(3)
        # self.logger.info("*****Search the Sales Product*****")
        # self.eqp.SearchButton()
        # time.sleep(3)
        # self.logger.info("*****Click the Product Checkbox*****")
        # self.eqp.ProductCheckbox()
        # time.sleep(3)
        # self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        # self.eqp.SelectButton()
        # time.sleep(2)
        # self.logger.info("*****Click The Add Products Button *****")
        # self.eqp.AddProdButton()
        # time.sleep(3)
        # self.logger.info("*****Lookup a Sales Product*****")
        # self.eqp.SearchField(self.searchitem3)
        # time.sleep(3)
        # self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        # self.eqp.SearchButton()
        # time.sleep(5)
        # self.logger.info("*****Click the Product Checkbox*****")
        # self.eqp.ProductCheckbox()
        # time.sleep(2)
        # self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        # self.eqp.SelectButton()
        # time.sleep(5)
        # self.logger.info("*****Click the Save Button*****")
        # self.eqp.SaveButton()
        # # time.sleep(4)
        # self.logger.info("*****Click the Submit For Approval Button*****")
        # self.qp.clickSubFApproval()
        # time.sleep(7)
        self.logger.info("*****Click the Generate Quote Button*****")
        self.qp.clickGenQuote()
        time.sleep(20)
        self.logger.info("*****Switch to the New Documents Window*****")
        self.driver.switch_to.frame(0)
        time.sleep(10)
        #print(name)
        self.logger.info("*****Click the Send For Signature Button*****")
        self.qp.SendFSigna()
        time.sleep(20)
        self.logger.info("*****Click the Next Button*****")
        self.qp.DocuSNext()
        time.sleep(20)
        self.logger.info("*****Click the Next Button*****")
        self.qp.DocuSNext()
        time.sleep(20)
        self.logger.info("*****Click Send to Customer Button****")
        self.qp.CustomerSend()
        time.sleep(20)
        self.logger.info("*****Sales Quote Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/SalesDocuSignpage.png")
        self.driver.quit()














