import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.EditQuotePage import EditQuotePage
from Pages.LoginPage import LoginPage
from Pages.ProductFilterPage import ProductFilterPage
from Pages.PartProdLinePage import PartProdLinePage
from Pages.QuotePage import QuotePage
from Pages.ToolProdLinePage import ToolProdLinePage
from Pages.ToolBoomLift import ToolBoomLiftPage
from Pages.ToolForkLift import ToolForkLiftPage
from Pages.ToolScissorLift import ToolScissorLiftPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_Tools:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    def test_Tools(self, setup):
        self.logger.info("*****Starting The Tools Test*****")
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

        # Define QuotePage Driver
        self.logger.info("****** QuotePage Driver Defined ******")
        self.qp = QuotePage(self.driver)
        self.logger.info("****** Click the CPQ Quotes Tab ******")
        self.qp.clickCpqQuoteTab()
        self.logger.info("****** Click a Quote Id ******")
        self.qp.clickQuote1()
        self.logger.info("****** Click the Edit Lines Button ******")
        self.qp.clickEditlines()

        # Define ProductFilterPage Driver
        self.logger.info("****** ProductFilterPage Driver Defined ******")
        self.prf = ProductFilterPage(self.driver)

        # Define EditQuotePage Driver
        self.logger.info("****** EditQuotePage Driver Defined ******")
        self.eqp = EditQuotePage(self.driver)
        self.driver.switch_to.frame(0)
        # self.driver.get("https://onpointgroup--opgsit--sbqq.sandbox.vf.force.com/apex/sb?id=a2dDP000001UhlnYAC&tour=&isdtp=p1&sfdcIFrameOrigin=https://onpointgroup--opgsit.sandbox.lightning.force.com&sfdcIFrameHost=web&nonce=76b1fa350d6223d8ca411bca9996596178b4375a59afb95a6139dc63e1954a3b&ltn_app_id=06mDP000000LwVFYA0&clc=0#quote/le?qId=a2dDP000001UhlnYAC")
        time.sleep(5)
        self.logger.info("****** Click the Add Products Button ******")
        self.eqp.AddProdButton()
        self.logger.info("****** Select the Offering Type Tool ******")
        self.eqp.OfferTypeTool()
        self.logger.info("****** Select the Product Family Boom Lift ******")
        self.prf.PrdFamBoomLft()

        # Define ToolProdLinePage Driver
        self.logger.info("****** ToolProdLinePage Driver Defined ******")
        self.tpl = ToolProdLinePage(self.driver)
        self.logger.info("****** Select the Product Line Option United ******")
        self.tpl.ToolUnitedBoomLift()
        time.sleep(3)
        self.logger.info("****** Click the Apply Button ******")
        self.eqp.ApplyButton()
        time.sleep(3)

        # Define ToolBoomLiftPage Driver
        self.logger.info("****** ToolProdLinePage Driver Defined ******")
        self.tbl = ToolBoomLiftPage(self.driver)
        self.logger.info("****** Select the United Rentals - BOOM 30-33' ARTICULATING DC Product******")
        self.tbl.TL1000()
        time.sleep(3)
        self.logger.info("****** Select the United Rentals - BOOM 65-70' TELESCOPIC Product******")
        self.tbl.TL1012()
        time.sleep(3)
        self.tbl.TL1014scroll()
        time.sleep(3)
        self.logger.info("****** Select the United Rentals - BOOM 120' TELESCOPIC 4WD Product******")
        self.tbl.TL1014()
        time.sleep(3)
        self.logger.info("****** Click the Filter Button ******")
        self.eqp.FilterButton()
        time.sleep(3)
        self.logger.info("****** Click the Product Filter Entry ******")
        self.eqp.ClearFieldButton()
        time.sleep(5)

        # Define ToolForkLiftPage Driver
        self.tfl = ToolForkLiftPage(self.driver)
        self.logger.info("****** ToolProdLinePage Driver Defined ******")
        self.tpl = ToolProdLinePage(self.driver)
        time.sleep(3)
        self.logger.info("****** Select the Offering Type Tool ******")
        self.eqp.OfferTypeTool()
        time.sleep(3)
        self.logger.info("****** Select the Product Family Boom Lift ******")
        self.prf.PrdFamFrklift()
        time.sleep(3)
        self.logger.info("****** Select the Product Line Option United ******")
        self.tpl.ToolUnitedForkLift()
        time.sleep(3)
        self.logger.info("****** Click the Apply Button ******")
        self.eqp.ApplyButton()
        time.sleep(3)
        self.logger.info("****** Select the United Rentals - FORKLIFT WHSE 5000# GAS/LP Product******")
        self.tfl.TL1027()
        time.sleep(3)
        self.logger.info("****** Select the United Rentals - FORKLIFT WHSE 8000# GAS/LP Product******")
        self.tfl.TL1031()
        time.sleep(3)
        self.tfl.TL1038scroll()
        time.sleep(3)
        self.logger.info("****** Select the United Rentals - FORKLIFT VARIABLE REACH 10000# 50' & UP Product******")
        self.tfl.TL1038()
        time.sleep(3)
        self.logger.info("****** Click the Filter Button ******")
        self.eqp.FilterButton()
        time.sleep(3)
        self.logger.info("****** Click the Product Filter Entry ******")
        self.eqp.ClearFieldButton()
        time.sleep(5)

        # Define ToolForkLiftPage Driver
        self.tsl = ToolScissorLiftPage(self.driver)
        self.logger.info("****** ToolProdLinePage Driver Defined ******")
        self.tpl = ToolProdLinePage(self.driver)
        self.logger.info("****** Select the Offering Type Tool ******")
        self.eqp.OfferTypeTool()
        time.sleep(3)
        self.logger.info("****** Select the Product Family Boom Lift ******")
        self.prf.PrdFamScislift()
        time.sleep(3)
        self.logger.info("****** Select the Product Line Option United ******")
        self.tpl.ToolUnitedScissorLift()
        time.sleep(3)
        self.logger.info("****** Click the Apply Button ******")
        self.eqp.ApplyButton()
        time.sleep(3)
        self.logger.info("****** Select the United Rentals - SCISSOR LIFT 19' ELECTRIC Product******")
        self.tsl.TL1015()
        time.sleep(3)
        self.logger.info("****** Select the United Rentals - SCISSOR LIFT 30-33' ELECTRIC 32 WIDE Product******")
        self.tsl.TL1020()
        time.sleep(3)
        self.logger.info("****** Select the United Rentals - FORKLIFT VARIABLE REACH 10000# 50' & UP Product******")
        self.tsl.TL1025scroll()
        time.sleep(3)
        self.tsl.TL1025()
        time.sleep(20)




