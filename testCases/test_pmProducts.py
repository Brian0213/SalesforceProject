import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.LoginPage import LoginPage
from Pages.QuotePage import QuotePage
from Pages.PMProductsPage import PMProductsPage
from Pages.RentalPage import RentalPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_PMProducts:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    travelitem = "Travel"
    dockitem = "PM1000"
    dockitem1 = "PM1001"
    dockitem2 = "PM1002"
    dockitem3 = "PM1003"
    dockitem4 = "PM1004"
    dockitem5 = "PM1005"
    dockitem6 = "PM1006"
    dockitem7 = "PM1007"
    dockitem8 = "PM1008"
    dockitem9 = "PM1009"
    dockitem10 = "PM1010"
    dockitem11 = "PM1011"
    dockitem12 = "PM1052"
    dooritem = "PM1012"
    dooritem1 = "PM1013"
    dooritem2 = "PM1014"
    dooritem3 = "PM1015"
    dooritem4 = "PM1016"
    dooritem5 = "PM1017"
    dooritem6 = "PM1018"
    dooritem7 = "PM1019"
    dooritem8 = "PM1020"
    dooritem9 = "PM1021"
    dooritem10 = "PM1022"
    dooritem11 = "PM1023"
    dooritem12 = "PM1024"
    dooritem13 = "PM1025"
    dooritem14 = "PM1026"
    dooritem15 = "PM1027"
    dooritem16 = "PM1028"
    dooritem17 = "PM1029"
    dooritem18 = "PM1030"
    dooritem19 = "PM1031"
    dooritem20 = "PM1032"
    dooritem21 = "PM1033"
    dooritem22 = "PM1034"
    dooritem23 = "PM1035"
    dooritem24 = "PM1036"
    dooritem25 = "PM1037"
    dooritem26 = "PM1038"
    dooritem27 = "PM1039"
    dooritem28 = "PM1051"
    gateitem = "PM1040"
    gateitem1 = "PM1041"
    gateitem2 = "PM1042"
    gateitem3 = "PM1043"
    gateitem4 = "PM1044"
    specialtyitem = "PM1045"
    wasteitem = "PM1046"
    wasteitem1 = "PM1047"
    wasteitem2 = "PM1048"
    wasteitem3 = "PM1049"
    wasteitem4 = "PM1050"
    materialitem = "TL1040"
    materialitem1 = "TL1041"
    materialitem2 = "TL1042"
    forkitem = "TL1026"
    forkitem1 = "TL1027"
    forkitem2 = "TL1028"
    forkitem3 = "TL1029"
    forkitem4 = "TL1030"
    forkitem5 = "TL1031"
    forkitem6 = "TL1032"
    forkitem7 = "TL1033"
    forkitem8 = "TL1034"
    forkitem9 = "TL1035"
    forkitem10 = "TL1036"
    forkitem11 = "TL1037"
    forkitem12 = "TL1038"
    forkitem13 = "TL1039"
    boomitem = "TL1000"
    boomitem1 = "TL1001"
    boomitem2 = "TL1002"
    boomitem3 = "TL1003"
    boomitem4 = "TL1004"
    boomitem5 = "TL1005"
    boomitem6 = "TL1006"
    boomitem7 = "TL1007"
    boomitem8 = "TL1008"
    boomitem9 = "TL1009"
    boomitem10 = "TL1010"
    boomitem11 = "TL1011"
    boomitem12 = "TL1012"
    boomitem13 = "TL1013"
    boomitem14 = "TL1014"
    boomitem15 = "TL1015"
    # scissoritem = "EXP006"
    scissoritem1 = "TL1015"
    scissoritem2 = "TL1016"
    scissoritem3 = "TL1017"
    scissoritem4 = "TL1018"
    scissoritem5 = "TL1019"
    scissoritem6 = "TL1020"
    scissoritem7 = "TL1021"
    scissoritem8 = "TL1022"
    scissoritem9 = "TL1023"
    scissoritem10 = "TL1024"
    scissoritem11 = "TL1025"
    toolsitem = "TL1043"
    toolsitem1 = "TL1044"
    toolsitem2 = "TL1045"
    toolsitem3 = "TL1046"
    toolsitem4 = "TL1047"
    toolsitem5 = "TL1048"
    toolsitem6 = "TL1049"
    toolsitem7 = "TL1050"
    toolsitem8 = "TL1051"
    toolsitem9 = "TL1052"
    toolsitem10 = "TL1053"
    toolsitem11 = "TL1054"
    toolsitem12 = "TL1055"
    toolsitem13 = "TL1056"
    toolsitem14 = "TL1057"
    toolsitem15 = "TL1058"
    toolsitem16 = "TL1059"
    toolsitem17 = "TL1060"
    toolsitem18 = "TL1061"
    toolsitem19 = "TL1062"
    toolsitem20 = "TL1063"
    toolsitem21 = "TL1064"


    def test_PMProducts(self, setup):
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

        self.logger.info("*****Starting The Rental Test*****")
        self.ltp = RentalPage(self.driver)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(3)
        self.logger.info("*****Click The Apply Button*****")
        self.ltp.ApplyButton()
        time.sleep(3)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(3)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(3)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem1)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(3)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(3)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(2)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem2)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(3)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem3)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem4)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem5)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem6)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem7)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(3)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(3)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(3)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem8)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(3)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(3)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(2)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem9)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(3)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem10)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem11)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem12)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem13)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Rental Product*****")
        self.ltp.SearchRental(self.boomitem14)
        time.sleep(3)
        self.logger.info("*****Search the Rental Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Labor Product*****")
        self.ltp.SearchRental(self.boomitem15)
        time.sleep(3)
        self.logger.info("*****Search the Labor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem1)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem2)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem3)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem4)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem5)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem6)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem7)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem8)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem9)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem10)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Scissor Product*****")
        self.ltp.SearchRental(self.scissoritem11)
        time.sleep(3)
        self.logger.info("*****Search the Scissor Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem1)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem2)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem3)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem4)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem5)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem6)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem7)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem8)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem9)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem10)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem11)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem12)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)
        self.logger.info("*****Click The Add Products Button *****")
        self.ltp.AddProdButton()
        time.sleep(3)
        self.logger.info("*****Lookup a Forklift Product*****")
        self.ltp.SearchRental(self.forkitem13)
        time.sleep(3)
        self.logger.info("*****Search the Forklift Product*****")
        self.ltp.SearchButton()
        time.sleep(5)
        self.logger.info("*****Click the Product Checkbox*****")
        self.ltp.ProductCheckbox()
        time.sleep(2)
        self.logger.info("*****Click the Select Button to Add the Product to the QLE*****")
        self.ltp.SelectButton()
        time.sleep(5)



        self.logger.info("*****Click the Save Button*****")
        self.ltp.SaveButton()
        time.sleep(5)
        self.logger.info("*****PM Products Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/PMProductspage.png")
        self.driver.quit()
