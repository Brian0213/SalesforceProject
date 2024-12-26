import time
import unittest

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.LoginPage import LoginPage
from Pages.EditQuotePage import EditQuotePage
from Pages.QuotePage import QuotePage
from Pages.ConfigureProductsPage import ConfigureProductsPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen
from selenium.webdriver.support import expected_conditions as EC

class Test_SalesCheck:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    opportunity = "MINOPPORTUNE0819-"
    party = "Meggitt (rockmart) Inc"
    contact = "Melissa Erickson"
    type = "Service - Commercial"
    subtype = "Repair"
    searchitem = "M202-1050"

    @pytest.mark.sales
    def test_salesCheck(self, setup):
        self.logger.info("*****Starting The Sales Opportunity Test*****")
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
        time.sleep(7)

        self.qp = QuotePage(self.driver)
        self.logger.info("*****Starting The Quote Page Test*****")
        # Click the CPQ Quote Tab
        self.qp.clickCpqQuoteTab()
        time.sleep(5)
        self.qp.SalesQuote1()
        time.sleep(4)
        self.qp.clickEditBtn()
        windowsIDs = self.driver.window_handles
        parentwindowid = windowsIDs[0]
        childwindowid = windowsIDs[1]
        print(parentwindowid, childwindowid)
        self.driver.switch_to.window(childwindowid)
        time.sleep(4)
        self.driver.find_element(By.XPATH, '//input[@name="Deposit__c"]').send_keys(10)
        time.sleep(4)
        # self.driver.find_element(By.XPATH, "//button[@aria-label='Deposit Scope']").click()
        # self.driver.find_element(By.XPATH, '//button[@class="slds-combobox__input slds-input_faux fix-slds-input_faux slds-combobox__input-value"]').click()
        # self.driver.find_element(By.XPATH, "//div[@class='slds-combobox__form-element slds-input-has-icon slds-input-has-icon_right']").click()
        # self.driver.find_element(By.XPATH, '//button[@class-value="slds-combobox__input slds-input_faux fix-slds-input_faux slds-combobox__input-value"]').click()
        # time.sleep(4)
        # self.driver.find_element(By.XPATH, '//div[@class="slds-combobox slds-dropdown-trigger slds-dropdown-trigger_click"]').click()
        # time.sleep(4)
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'Material Only')]").click()
        # self.driver.execute_script("window.scrollBy(0, 900)")
        # Click the Edit Lines Button
        # self.qp.clickEditlines()
        # time.sleep(7)
        # # Switch to Frame
        # self.driver.switch_to.frame(0)
        #
        # self.logger.info("*****Starting The Quote Line Editor Test*****")
        # self.eqp = EditQuotePage(self.driver)
        # self.cpp = ConfigureProductsPage(self.driver)
        # self.cpp.clickReconfigureRow2()
        # time.sleep(3)
        # self.cpp.ReconExpense()
        # time.sleep(3)
        # self.cpp.ReSurcharge()
        # self.logger.info("*****Click The Add Products Button *****")
        # self.eqp.AddProdButton()
        # time.sleep(3)
        # self.logger.info("*****Lookup a Sales Product*****")
        # self.eqp.SearchProduct(self.searchitem)
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
        # time.sleep(5)
        # self.cpp.clickReconfigure()
        # time.sleep(3)
        # self.cpp.ReconLabor()
        # time.sleep(3)
        # self.cpp.ReLabManStand()
        # time.sleep(3)
        # self.cpp.ReLabManOverT()
        # time.sleep(3)
        # self.cpp.ReLabManDoubleT()
        # time.sleep(3)
        # self.cpp.ReLabManEmergencyT()
        # time.sleep(3)
        # self.cpp.ReAddManDoubleT()
        # time.sleep(3)
        # self.cpp.ReAddManOverT()
        # time.sleep(3)
        # self.cpp.ReAddManStandardT()
        # time.sleep(3)
        # self.driver.execute_script("window.scrollBy(0, 50)")
        # time.sleep(3)
        # self.cpp.ReAddManEmergencyT()
        # self.eqp.ReconSaveBtn()
        # self.logger.info("*****Click The Add Products Button *****")
        # self.eqp.AddProdButton()
        # time.sleep(3)
        # self.eqp.ApplyButton()
        # time.sleep(5)
        # iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='accessibility title']")))
        # time.sleep(10)
        # self.driver.switch_to.frame(iframe)
        # self.qp = QuotePage(self.driver)
        # windowsIDs = self.driver.window_handles
        # parentwindowid = windowsIDs[0]
        # childwindowid = windowsIDs[1]
        # print(parentwindowid, childwindowid)
        # self.driver.switch_to.window(childwindowid)
        # self.driver.execute_script("window.scrollBy(0, 250)")
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Opportunities']")))
        # time.sleep(3)
        # self.eqp.OtherProducts()
        # # Click the Opportunity Tab
        # self.qp.clickCpqQuoteTab()
        # time.sleep(3)
        # # Click on an Opportunity ID
        # self.qp.SalesQuote1()
        # time.sleep(3)
        # self.driver.execute_script("window.scrollBy(0, 150)")
        # time.sleep(3)
        # Opportunity Assertions
        # stage = self.driver.find_element(By.XPATH, "//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11']").text
        # assert stage == "Closed Won Pending", "Stage Is Not Correct"
        # assert "Closed Won Pending" in stage, "Stage is Incorrect"
        # assert "Closed Won Pending" == "Closed Won Pending"
        # order = self.driver.find_element(By.XPATH, "//span[normalize-space()='Service - Commercial']").text
        # assert order == "Service - Commercial", "Order Type Is Not Correct"
        # assert "Service - Commercial" in order, "Order Type is Incorrect"
        # assert "Service - Commercial" == "Service - Commercial"
        # orderS = self.driver.find_element(By.XPATH, "//span[normalize-space()='Repair']").text
        # assert orderS == "Repair", "OrderS Is Not Correct"
        # assert "Repair" in orderS, "Order Type is Incorrect"
        # assert "Repair" == "Repair"
        # OpportunityR = self.driver.find_element(By.XPATH, "//span[normalize-space()='Miner Sales Opportunity']").text
        # assert OpportunityR == "Miner Sales Opportunity", "OpportunityR Is Not Correct"
        # assert "Miner Sales Opportunity" in OpportunityR, "OpportunityR is Incorrect"
        # assert "Miner Sales Opportunity" == "Miner Sales Opportunity"
        # Quote Assertions
        # OpportunityQ = self.driver.find_element(By.XPATH, "//slot[contains(text(),'MINOPPORTUNE0819-')]").text
        # assert OpportunityQ == "MINOPPORTUNE0819-", "MINOPPORTUNE0819- Is Not Correct"
        # assert "MINOPPORTUNE0819-" in OpportunityQ, "MINOPPORTUNE0819- Is Incorrect"
        # assert "MINOPPORTUNE0819-" == "MINOPPORTUNE0819-"
        # PayingP = self.driver.find_element(By.XPATH, "//slot[contains(text(),'Georgia Aquarium, INC.')]").text
        # assert PayingP == "Georgia Aquarium, INC.", "Georgia Aquarium, INC. Is Not Correct"
        # assert "Georgia Aquarium, INC." in PayingP, "Georgia Aquarium, INC. Is Incorrect"
        # assert "Georgia Aquarium, INC." == "Georgia Aquarium, INC."
        # Location = self.driver.find_element(By.XPATH, "//slot[contains(text(),'Georgia Aquarium')]").text
        # assert Location == "Georgia Aquarium", "Georgia Aquarium Is Not Correct"
        # assert "Georgia Aquarium" in Location, "Georgia Aquarium Is Incorrect"
        # assert "Georgia Aquarium" == "Georgia Aquarium"
        # PriCheckBox = self.driver.find_element(By.XPATH, "//span[[contains(text(),'Primary')]]")
        # assert PriCheckBox.is_selected(), "Primary Checkbox Is Not Correct"






        time.sleep(7)
        self.logger.info("*****Sales Opportunity Test Completed*****")
        self.driver.save_screenshot("/Users/oluwasegun.ojeyinka/PycharmProjects/ProjectHorizon/Screenshots/SalesCheckPage.png")
        self.logger.info("*****Close the Application and Browser*****")
        self.driver.quit()








        # loc_record = self.(By.XPATH, "//span[normalize-space()='LCR-025151']")





        # self.Op.clickNextBtn()
        #
        # self.driver.switch_to.frame(1)
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//article[@class='slds-is-relative']//flowruntime-navigation-bar[@class='slds-card__footer navigationBar']").click()
        # time.sleep(5)
        # Clicking the Location Record
        #self.driver.switch_to.frame("//flexipage-component2[@data-component-id='flexipage_tabset']//div[@class='slds-tabs_card']")
        #time.sleep(3)