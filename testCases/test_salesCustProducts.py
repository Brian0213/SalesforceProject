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

class Test_SalesAddCustomProducts:

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
    # searchitem3
    customitem = "CP101-0023"
    customitem2 = "CP200-0016"
    customitem3 = "CP500-0004"
    value = 10
    laboritem = "LB0001"
    travelitem = "LB1STR001"

    @pytest.mark.custe2e
    def test_SalesAddCustomProducts(self, setup):
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
        time.sleep(2)
        self.logger.info("*****Click the Edit Lines Button*****")
        self.qp.clickEditlines()
        time.sleep(7)
        self.logger.info("*****Switch to The Quote Line Editor*****")
        self.driver.switch_to.frame(0)

        self.logger.info("*****Starting The Quote Line Editor Test*****")
        self.eqp = EditQuotePage(self.driver)
        self.logger.info("*****Click The Add Products Button *****")
        self.eqp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Sales Product*****")
        self.eqp.SearchCustom(self.customitem)
        time.sleep(3)
        self.logger.info("*****Search the Custom Product*****")
        self.eqp.SearchButton()
        time.sleep(3)
        self.logger.info("*****Click The Apply Button*****")
        self.eqp.ApplyButton()
        time.sleep(3)
        self.logger.info("*****Click the Custom Product Checkbox*****")
        self.eqp.ProductCheckbox()
        time.sleep(3)
        self.logger.info("*****Click the Select Button to Add the Custom Product to the QLE*****")
        self.eqp.SelectButton()
        time.sleep(3)
        self.logger.info("*****Click The Add Products Button *****")
        self.eqp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Custom Product*****")
        self.eqp.SearchCustom(self.customitem2)
        time.sleep(3)
        self.logger.info("*****Search the Sales Product*****")
        self.eqp.SearchButton()
        time.sleep(3)
        self.logger.info("*****Click the Custom Product Checkbox*****")
        self.eqp.ProductCheckbox()
        time.sleep(3)
        self.logger.info("*****Click the Select Button to Add the Custom Product to the QLE*****")
        self.eqp.SelectButton()
        time.sleep(2)
        self.logger.info("*****Click The Add Products Button *****")
        self.eqp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Custom Product*****")
        self.eqp.SearchCustom(self.customitem3)
        time.sleep(3)
        self.logger.info("*****Search the Custom Product*****")
        self.eqp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Custom Product Checkbox*****")
        self.eqp.ProductCheckbox()
        time.sleep(3)
        self.logger.info("*****Click the Select Button to Add the Custom Product to the QLE*****")
        self.eqp.SelectButton()
        time.sleep(3)
        self.logger.info("*****Click The Add Products Button *****")
        self.eqp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Travel Product*****")
        self.eqp.SearchTravel(self.travelitem)
        time.sleep(3)
        self.logger.info("*****Search the Travel Product****")
        self.eqp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.eqp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.eqp.SelectButton()
        self.logger.info("*****Click The Add Products Button *****")
        self.eqp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Labor Product*****")
        self.eqp.SearchLabor(self.laboritem)
        time.sleep(3)
        self.logger.info("*****Search the Labor Product*****")
        self.eqp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.eqp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.eqp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click the Save Button*****")
        self.eqp.SaveButton()
        time.sleep(4)
        # self.logger.info("*****Click the Submit For Approval Button*****")
        # self.qp.clickSubFApproval()
        # time.sleep(7)
        # self.logger.info("*****Click the Generate Quote Button*****")
        # self.qp.clickGenQuote()
        # time.sleep(25)
        # self.logger.info("*****Switch to the New Documents Window*****")
        # self.driver.switch_to.frame(0)
        # time.sleep(10)
        # #print(name)
        # self.logger.info("*****Click the Send For Signature Button*****")
        # self.qp.SendFSigna()
        # time.sleep(20)
        # self.logger.info("*****Click the Next Button*****")
        # self.qp.DocuSNext()
        # time.sleep(20)
        # self.logger.info("*****Click the Next Button*****")
        # self.qp.DocuSNext()
        # time.sleep(20)
        # self.logger.info("*****Click Send to Customer Button****")
        # self.qp.CustomerSend()
        # time.sleep(30)
        time.sleep(15)
        self.logger.info("*****Sales Quote Add Custom Product Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/SalesAddProductspage.png")
        self.driver.quit()














        # self.driver.get("https://onpointgroup--opgsit--sbqq.sandbox.vf.force.com/apex/sb?id=a2dWr000000bprZIAQ&tour=&isdtp=p1&sfdcIFrameOrigin=https://onpointgroup--opgsit.sandbox.lightning.force.com&sfdcIFrameHost=web&nonce=5d7deea4f8a93f237de53af58d243f4a57a6453236ffbb673d528aa4b404e960&ltn_app_id=06mDP000000LwVFYA0&clc=0#quote/le?qId=a2dWr000000bprZIAQ")
        # # self.driver.get("https://onpointgroup--opgsit--sbqq.sandbox.vf.force.com/apex/sb?id=a2dDP000001UhlnYAC&tour=&isdtp=p1&sfdcIFrameOrigin=https://onpointgroup--opgsit.sandbox.lightning.force.com&sfdcIFrameHost=web&nonce=76b1fa350d6223d8ca411bca9996596178b4375a59afb95a6139dc63e1954a3b&ltn_app_id=06mDP000000LwVFYA0&clc=0#quote/le?qId=a2dDP000001UhlnYAC")
        # time.sleep(3)





         # # self.driver.get("https://onpointgroup--opgsit.sandbox.lightning.force.com/lightning/r/SBQQ__Quote__c/a2dDP000001UhlnYAC/view")
        # self.driver.get("https://onpointgroup--opgsit.sandbox.lightning.force.com/lightning/r/SBQQ__Quote__c/a2dWr000000bprZIAQ/view")
        #time.sleep(5)
