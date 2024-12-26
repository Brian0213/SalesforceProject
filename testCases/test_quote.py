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

class Test_Quote:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()
    searchitem = "Sub Labor for Door - Coiling Steel Operator"

    def test_Quote(self, setup):
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

        #self.hp = HomePage(self.driver)
        #self.hp.clickReportsTab()
        #time.sleep(10)

        #self.Op = OpportunityPage(self.driver)
        #self.Op.clickAccountTab()

        self.qp = QuotePage(self.driver)
        #self.qp.clickOpportunityTab()
        #self.qp.clickOpportunityID()
        #self.qp.clickNewQuoteId()
        #self.qp.setQuoteName(self.quotename)
        #self.qp.clickQuoteButton()
        self.qp.clickCpqQuoteTab()
        #time.sleep(5)
        self.qp.clickQuote()
        #time.sleep(5)
        #self.qp.clickEditB()
        #time.sleep(5)
        self.qp.clickEditlines()
        # frames = self.driver.find_elements(By.TAG_NAME, "iFrame")
        # print("There are", len(frames), "frames on this web page.")
        # for f in frames:
        #     print("Frame Id:", f.get_attribute('id'), "Frame Name:", f.get_attribute('name'))
        #self.qp.clickPrevApproval()
        #self.qp.clickSubFApproval()
        #self.qp.clickRecApproval()
        self.driver.switch_to.frame(1)
        time.sleep(5)

        self.eqp = EditQuotePage(self.driver)
        #self.driver.get("https://onpointgroup--opgsit--sbqq.sandbox.vf.force.com/apex/sb?id=a2dDP000001Uhf7YAC&tour=&isdtp=p1&sfdcIFrameOrigin=https://onpointgroup--opgsit.sandbox.lightning.force.com&sfdcIFrameHost=web&nonce=8847231c4549455e323bbdbe8ca6194c35dd3d56d7b1c3a153e0498086c9c8a2&ltn_app_id=06mDP000000LwVFYA0&clc=0#quote/le?qId=a2dDP000001Uhf7YAC")
        time.sleep(2)
        self.eqp.AddProdButton()
        time.sleep(2)
        self.eqp.SearchField(self.searchitem)
        time.sleep(2)
        self.eqp.SearchButton()
        time.sleep(2)
        # self.eqp.OfferTypePart()
        # time.sleep(2)
        # self.eqp.FilterButton()
        # time.sleep(5)
        self.eqp.ApplyButton()
        time.sleep(10)

        self.pfp = ProductFilterPage(self.driver)
        # self.pfp.PrdFamAEDPart()
        # time.sleep(3)

        self.ppl = PartProdLinePage(self.driver)
        # self.ppl.AEDPedDoor()
        # time.sleep(3)
        # self.eqp.ClearFieldButton()
        # time.sleep(5)








