from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

class OpportunityPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def clickAccountTab(self):
        account_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Accounts']")))
        self.driver.execute_script("arguments[0].click();", account_tab)

    def clickOpportunityTab(self):
        opportunity_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Opportunities']")))
        self.driver.execute_script("arguments[0].click();", opportunity_tab)

    def clickAccountName(self):
        account_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Georgia Aquarium, INC.']")))
        self.driver.execute_script("arguments[0].click();", account_name)

    def clickAccountNameUat(self):
        account_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Georgia Aquarium, INC.']")))
        self.driver.execute_script("arguments[0].click();", account_name)

    def clickLocRecord(self):
        loc_record=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='LCR-025151']")))
        self.driver.execute_script("arguments[0].click();", loc_record)

    def clickLocation(self):
        location=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Georgia Aquarium']")))
        self.driver.execute_script("arguments[0].click();", location)

    def clickLocationUat(self):
        location=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Georgia Aquarium For Testing')]")))
        self.driver.execute_script("arguments[0].click();", location)

    def clickLocIcon(self):
        loc_icon=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@title,'Show 7 more actions')]//lightning-primitive-icon")))
        self.driver.execute_script("arguments[0].click();", loc_icon)

    def clickNewOpp(self):
        new_opp=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='New Opportunity']")))
        self.driver.execute_script("arguments[0].click();", new_opp)

    def clickMinSales(self):
        min_sales=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Miner Sales Opportunity')]")))
        self.driver.execute_script("arguments[0].click();", min_sales)

    def clickMinPM(self):
        min_pm=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Miner PM Opportunity')]")))
        self.driver.execute_script("arguments[0].click();", min_pm)

    def clickFacServ(self):
        fac_serv=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//flowruntime-lwc-body/div[1]/flowruntime-list-container[1]/div[1]/flowruntime-base-section[1]/div[1]/flowruntime-screen-field[1]/flowruntime-lwc-field[1]/div[1]/flowruntime-radio-button-input-lwc[1]/fieldset[1]/div[1]/span[1]/label[1]/span[1]")))
        self.driver.execute_script("arguments[0].click();", fac_serv)

    def clickNext(self):
        next_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()
        self.driver.execute_script("arguments[0].click();", next_button)

    def enterOppName(self, opportunity):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Name']"))).send_keys(opportunity)

    def enterClosedate(self, date):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="CloseDate"]'))).send_keys(date)

    def lookupAccount(self, account):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(account)

    def lookupAccountUat(self, accountuat):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(accountuat)

    def selAccount(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="ContractingParty.1"]'))).click()

    def payParty(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="PayingPartyAccount"]/option[@value="PayingParty.1"]'))).click()

    def lookupAccountUat1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).click()

    def lookupAccount1(self, account):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(account)

    def lookupAccount11(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).click()

    def lookupAccountA(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.ARROW_DOWN)

    def lookupAccount2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.RETURN)

    def lookupAccount3(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.ENTER)

    def lookAcct(self):
        options=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-value="Miner"]')))
        options.click()

    def pickMiner(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Miner']"))).click()

    def pickAtlanat(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@placeholder='Miner']"))).click()

    def payingParty(self, party):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='PayingPartyAccount']"))).send_keys(party)

    def primaryContact(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search Contacts..."]'))).click()

    def primaryP(self):
        self.action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def primaryContact1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search Contacts..."]'))).send_keys(Keys.ARROW_DOWN)

    def primaryContact3(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search Contacts..."]'))).send_keys(Keys.ARROW_DOWN)

    def primaryContact4(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search Contacts..."]'))).send_keys(Keys.ARROW_DOWN)

    def primaryContact2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search Contacts..."]'))).send_keys(Keys.RETURN)

    def opportunitySuccess(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="slds-button slds-button_success"]'))).click()

    def orderType(self):
        ord_typ=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="slds-combobox__input slds-input_faux fix-slds-input_faux slds-combobox__input-value"]')))
        self.driver.execute_script("arguments[0].click();", ord_typ)

    def servcomm(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Service - Commercial')]"))).click()

    def orderSubType(self):
        typ_ord=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Order Sub Type - Current Selection: --None--"]')))
        self.driver.execute_script("arguments[0].click();", typ_ord)

    def pickSurvey(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Survey')]"))).click()

    def pickRepair(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Repair')]"))).click()

    def pickInstallation(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Installation')]"))).click()

    def pickHardware(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Hardware Only - Parts')]"))).click()

    def pickDiagnos(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Diagnostic Only')]"))).click()

    def repPick(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Repair')]"))).click()

    def newOppoPageButton(self):
        newOppPageBtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']")))
        self.driver.execute_script("arguments[0].click();", newOppPageBtn)

    def clickNextBtn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//lightning-button[@class='slds-button flow-button__NEXT']"))).click()

    def clickOppo(self):
        Oppid = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Aqua-Loc']")))
        self.driver.execute_script("arguments[0].click(true);", Oppid)

    def NewQuote(self):
        quotebtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='New CPQ Quote']")))
        self.driver.execute_script("arguments[0].click(true);", quotebtn)

    def servcomm(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Service - Commercial')]"))).click()

    def equipcomm(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Equipment - Commercial')]"))).click()

    def resident(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Residential')]"))).click()

    def pickConstGrd(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Construction - Ground up')]"))).click()

    def pickConstRemodel(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Construction - Remodel')]"))).click()

    def pickEndUserRemodel(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'End User - Remodel')]"))).click()

    def pickEquipMatOnly(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Equipment - Material Only')]"))).click()

    def primaryContact1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search Contacts..."]'))).click()

    def descriptionFieldScr(self):
        descfield=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Edit Description']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", descfield)

    def orderSub(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Order Sub Type"]'))).click()

    def orderSubScr(self):
        ordsubfield=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Order Sub Type"]')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ordsubfield)