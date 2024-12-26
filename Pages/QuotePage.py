from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class QuotePage:

    def __init__(self, driver):
        self.driver = driver

    def clickOpportunityTab(self):
        oppor_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Opportunities']")))
        self.driver.execute_script("arguments[0].click();", oppor_tab)

    def clickOpportunityIDPM(self):
        pmoppor_id=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='WEDSEP18']")))
        self.driver.execute_script("arguments[0].click();", pmoppor_id)

    def clickOpportunityIDSales(self):
        saloppor_id=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@title="OLUWASEGUN - DONT USE THIS.05"]')))
        self.driver.execute_script("arguments[0].click();", saloppor_id)

    def clickNewQuoteBtn(self):
        newquote_id=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='New CPQ Quote']")))
        self.driver.execute_script("arguments[0].click();", newquote_id)

    def clickEditBtn(self):
        edit_btn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="Edit"]')))
        self.driver.execute_script("arguments[0].click();", edit_btn)

    def description(self, fill):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@class="slds-textarea"]'))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@class="slds-textarea"]'))).send_keys(fill)

    def saveDescrip(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="SaveEdit"]'))).click()

    def setQuoteName(self, quotename):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='uiInput uiInputText uiInput--default uiInput--input']//input[@type='text']"))).send_keys(quotename)

    def clickQuoteButton(self):
        button_newquote=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper-body"]/footer/button[2]')))
        self.driver.execute_script("arguments[0].click(true);", button_newquote)

    def clickSave(self):
        button_quote=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="slds-button slds-button_brand cuf-publisherShareButton undefined uiButton"]')))
        self.driver.execute_script("arguments[0].click(true);", button_quote)

    def clickCpqQuoteTab(self):
        qte_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='slds-truncate'][normalize-space()='CPQ Quotes']")))
        self.driver.execute_script("arguments[0].click();", qte_tab)

    def SalesQuote(self):
        salesquote = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Q-11389']")))
        self.driver.execute_script("arguments[0].click(true);", salesquote)

    def SalesQuote1(self):
        salesquote = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Q-13737']")))
        self.driver.execute_script("arguments[0].click(true);", salesquote)

    def PMQuote(self):
        pmquote = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='slds-truncate'][normalize-space()='Q-07202']")))
        self.driver.execute_script("arguments[0].click(true);", pmquote)

    def PMQuote1(self):
        pmquote = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Q-11710']")))
        self.driver.execute_script("arguments[0].click(true);", pmquote)

    def clickEditB(self):
        editb = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Edit')]")))
        self.driver.execute_script("arguments[0].click(true);", editb)

    def clickEditlines(self):
        editL=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Edit Lines')]")))
        self.driver.execute_script("arguments[0].click(true);", editL)

    def clickPrevApproval(self):
        preA=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Preview Approval')]")))
        self.driver.execute_script("arguments[0].click(true);", preA)

    def clickSubFApproval(self):
        subA=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='slds-button slds-button_neutral'][normalize-space()='Submit for Approval']")))
        self.driver.execute_script("arguments[0].click(true);", subA)

    def clickSubFApprovalUat(self):
        subA=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit for Approval']")))
        self.driver.execute_script("arguments[0].click(true);", subA)

    def clickDelete(self):
        delT=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Delete')]")))
        self.driver.execute_script("arguments[0].click(true);", delT)

    def clickGenQuote(self):
        genQ=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Generate Quote')]")))
        self.driver.execute_script("arguments[0].click(true);", genQ)

    def clickGenOHQuote(self):
        genOHQ=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Generate Overhead Quote')]")))
        self.driver.execute_script("arguments[0].click(true);", genOHQ)

    def clickRecApproval(self):
        recA=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Recall Approval')]")))
        self.driver.execute_script("arguments[0].click(true);", recA)

    def clickCreateWO(self):
        crO=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Create Work Order')]")))
        self.driver.execute_script("arguments[0].click(true);", crO)

    def qleAddProducts(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="actions"]/sb-custom-action[1]'))).click()

    def SendFSigna(self):
        send=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send for Signature']")))
        self.driver.execute_script("arguments[0].click();", send)

    def DocuSNext(self):
        doc=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']")))
        self.driver.execute_script("arguments[0].click();", doc)

    def CustomerSend(self):
        custemail = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='olv-button olv-ignore-transform css-wo5tll']")))
        self.driver.execute_script("arguments[0].click();", custemail)

    def ApprovallinkMgr1(self):
        approvalid = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Approvals')]")))
        self.driver.execute_script("arguments[0].click();", approvalid)

    def ApprovallinkMgr2(self):
        approvalid = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'A-00521')]")))
        self.driver.execute_script("arguments[0].click();", approvalid)

    def ApprovallinkVP(self):
        approvalid = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'A-00518')]")))
        self.driver.execute_script("arguments[0].click();", approvalid)

    def ApprovalBtn(self):
        approvalbtn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Approve']")))
        self.driver.execute_script("arguments[0].click();", approvalbtn)

    def EnterApproveNote(self, note):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='j_id0:j_id5:j_id35:textarea-input-01']"))).send_keys(note)

    def ApproveComplete(self):
        approvalcpt = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='j_id0:j_id5:j_id35:j_id39']")))
        self.driver.execute_script("arguments[0].click();", approvalcpt)

    def clickPMPlantab(self):
        pmplantab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//slot[normalize-space()='Maintenance Plans (1)']")))  #//slot[normalize-space()='Maintenance Plans (1)']  #//span[contains(text(),'Maintenance Plans')]
        self.driver.execute_script("arguments[0].click(true);", pmplantab)

    def clickPMPlanId(self):
        pmplanid = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//slot[contains(text(),'MP-0910')]")))
        self.driver.execute_script("arguments[0].click(true);", pmplanid)

    def clickPMEdit(self):
        editid = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="MaintenancePlan.Generate_Work_Order"]')))
        self.driver.execute_script("arguments[0].click(true);", editid)

    def genWO(self):
        genwo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="MaintenancePlan.Generate_Work_Order"]')))
        self.driver.execute_script("arguments[0].click(true);", genwo)

    def nxtCreate(self):
        nxt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="slds-button slds-button_brand"]')))
        self.driver.execute_script("arguments[0].click(true);", nxt)

    def clickFinish(self):
        fnh = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//lightning-button[@class="slds-button flow-button__FINISH"]')))
        self.driver.execute_script("arguments[0].click(true);", fnh)

    def clickWOTab(self):
        wotab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="slds-button slds-button_icon slds-button_icon-bare"]')))
        self.driver.execute_script("arguments[0].click(true);", wotab)

    def clickWOTAB1(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[2]//div[2]//div[1]//div[1]//div[1]//div[1]//div[4]//div[1]//div[1]//one-record-home-flexipage2[1]//forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-maintenance_-plan_-record_-page___-maintenance-plan___-v-i-e-w[1]//forcegenerated-flexipage_maintenance_plan_record_page_maintenanceplan__view_js[1]//record_flexipage-desktop-record-page-decorator[1]//div[1]//records-record-layout-event-broker[1]//slot[1]//slot[1]//flexipage-record-home-template-desktop2[1]//div[1]//div[1]//slot[1]//flexipage-component2[2]//slot[1]//lst-related-list-quick-links-container[1]//article[1]//laf-progressive-container[1]//slot[1]//lst-related-list-quick-links-grid[1]//div[1]//div[1]//ul[1]//li[3]//lst-related-list-quick-link[1]//div[1]//div[1]//records-hoverable-link[1]//div[1]//a[1]//slot[1]//span[1]"))).click()

    def clickPMPWOtab(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//slot[normalize-space()='Work Orders (1)']"))).click()
    def clickWorkOrderID(self):
        woid=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='00062778']")))
        self.driver.execute_script("arguments[0].click();", woid)

    def clickPen(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="detailTab__item"]//button[@title="Edit Approval Status"]'))).click()

    def clickApprovePen(self):
        apst=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-target-selection-name="sfdc:RecordField.MaintenancePlan.Approval_Status__c"]')))
        self.driver.execute_script("arguments[0].click(true);", apst)

    def clickEdit(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[class="slds-assistive-text"]'))).click()

    def descriptionFieldScr(self):
        descfield=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Edit Description']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", descfield)

    def clickDescripPen(self):
        descpin=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Edit Description']")))
        self.driver.execute_script("arguments[0].click(true);", descpin)

    def clnDescrip(self):
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]'))).click()
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]//textarea[@="slds-textarea"]'))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]'))).clear()

    def fillDescrip1(self):
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]'))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]//textarea[@="slds-textarea"]'))).clear()
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]'))).send_keys(noted)

    def fillDescrip(self, noted):
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]'))).click()
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]//textarea[@="slds-textarea"]'))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]'))).send_keys(noted)

    def saveDescriptionEdit(self):
        descfield=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="SaveEdit"]')))
        self.driver.execute_script("arguments[0].click(true);", descfield)

    def amendButton(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="SBQQ__Quote__c.Amended_Quote"]'))).click()

    def amendCustChange(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Amend_Quote_Reason_Picklist.Customer Change"]'))).click()

    def amendBuChange(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Amend_Quote_Reason_Picklist.BU Change"]'))).click()

    def amendNoeRequested(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Amend_Quote_Reason_Picklist.NOE Requested"]'))).click()

    def amendComplete(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper-body"]/div[2]/div/article/flowruntime-flow/flowruntime-navigation-bar/footer/div[2]/lightning-button/button'))).click()

    def relatedTab(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='relatedListsTab__item']"))).click()

    def mainAsset(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='window']//slot[contains(text(),'MA-1406')]"))).click()

    def Check(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='lgt-dt-header-factory-id-1950']//span[@class='slds-checkbox_faux']"))).click()

    def details(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='detailTab__item']"))).click()

    def OppEdit(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='Edit']"))).click()

    def winDescrip(self, descrip):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]/textarea[@class="slds-textarea"]'))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="slds-form-element__control slds-grow textarea-container"]/textarea[@class="slds-textarea"]'))).send_keys(descrip)

    def cloneNavArr(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='slds-button slds-button_icon-border-filled fix-slds-button_icon-border-filled slds-button_last']"))).click()

    def cloneRelatedQuote(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Clone with Related']"))).click()

    def cloneQuote(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageTitle"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "#sbPageTitleTable']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#icon iconCustom sbHeaderIcon").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#sbPageTitleLeft").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#sbPageTitleRight").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#sbBtns").shadow_root

    def CancelButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "sbPageTitle"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sbBtns").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, '[onclick="cloneOnClick(this); return false;"]').click()

    def cloneRelatedQuote1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="sbBtns"]//input[@value="Clone"]'))).click()

    def quoteDescription(self, infor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ql-editor ql-blank slds-rich-text-area__content slds-text-color_weak slds-grow']"))).send_keys(infor)



