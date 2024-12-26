from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class NewServiceWOPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def clickAccountTab(self):
        account_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Accounts']")))
        self.driver.execute_script("arguments[0].click();", account_tab)

    def clickAccountName(self):
        account_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Meggitt (rockmart) Inc']")))
        self.driver.execute_script("arguments[0].click();", account_name)

    def clickLocation(self):
        wo_btn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Meggitt (Rockmart) Inc ()']")))
        self.driver.execute_script("arguments[0].click();", wo_btn)

    def serviceWOBtn(self):
        wo_btn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@title="New Service Work Order"]')))
        self.driver.execute_script("arguments[0].click();", wo_btn)

    def workOrderSubject(self, woid):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Work_Order_Subject"]'))).send_keys(woid)

    def selectSiteContact(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Select_a_Site_Contact"]'))).click()

    def selectSiteContactNotList(self):
        sitecontact= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Select_a_Site_Contact"]'))))
        sitecontact.select_by_visible_text("Not Listed")

    def selectAPContact(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Select_AP_Contact"]'))).click()

    def selectAPContactNotList(self):
        apcontact= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Select_AP_Contact"]'))))
        apcontact.select_by_visible_text("Not Listed")

    def siteContact(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).click()

    def siteContact1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.ARROW_DOWN)

    def siteContact2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.RETURN)

    def siteContact3(self):
        self.action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def apContact(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).click()


    def orderType(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select-1244"))).click()

    def orderTypeRES(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Residental"]'))).click()

    def orderTypeEquip(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Equipment - Commercial"]'))).click()

    def orderTypeServ(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Service - Commercial"]'))).click()

    def subOrderType(self):
        suborder=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]')))
        self.driver.execute_script("arguments[0].click(true);", suborder)

    def subTypeRESMatOnly(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Material Only"]'))).click()

    def subTypeRESServ(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Service"]'))).click()

    def subTypeRESEquip(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Equipment"]'))).click()

    def subTypeEquipCGrd(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Construction - Ground Up"]'))).click()

    def subTypeEquipCRmd(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Construction - Remodel"]'))).click()

    def subTypeEquipERmd(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="End User - Remodel"]'))).click()

    def subTypeEquipEmd(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Equipment - Material Only"]'))).click()

    def subTypeServDO(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Diagnostic Only"]'))).click()

    def subTypeServHard(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Hardware Only - Parts"]'))).click()

    def subTypeScr(self):
        field=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)

    def subTypeServInstall(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Installation"]'))).click()

    def subTypeServPM(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Proactive Maintenance"]'))).click()

    def subTypeServRP(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Repair"]'))).click()

    def subTypeServSur(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Survey"]'))).click()

    def pickky(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="slds-select"]/option[4]'))).click()

    def pickInstallation(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Installation"]'))).click()

    def equipTypeDock(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Dock"]'))).click()

    def equipTypeDoor(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Door"]'))).click()

    def equipTypeGate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Gate"]'))).click()

    def equipTypeGenHard(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="General Hardware"]'))).click()

    def equipTypeMhe(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="MHE"]'))).click()

    def equipTypeSpecialty(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Specialty"]'))).click()

    def equipTypeWaste(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Waste"]'))).click()

    def equipTypeAEDPrt(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="AED Part"]'))).click()

    def equipTypeBoomLft(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Boom Lift"]'))).click()

    def equipTypeForklft(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Forklift"]'))).click()

    def equipTypeMatLift(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Material Lift"]'))).click()

    def equipTypeScissLift(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Scissor Lift"]'))).click()

    def equipTypePos(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Position"]'))).click()

    def equipTypeMisc(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="Miscellaneous"]'))).click()

    def probDescription(self, fillin):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@class="slds-textarea"]'))).send_keys(fillin)

    def priorEarliest(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="chPriority.At Earliest Availability"]'))).click()

    def prior24Hour(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="chPriority.24 Hour Response"]'))).click()

    def priorSameDayService(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="chPriority.Same Day Service"]'))).click()

    def priorEmergency(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="slds-select"]/option[@value="chPriority.Emergency (4 Hours)"]'))).click()

    def labSrcMiner(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Labor_Source"]/option[@value="chLaborSource.Miner"]'))).click()

    def labSrcSubcontracted(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Labor_Source"]/option[@value="chLaborSource.Subcontracted"]'))).click()

    def scissLiftReq(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="slds-checkbox_faux"]'))).click()

    def custScissLift(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="slds-checkbox"]/input[@name="scrCan_we_use_Customer_s_Scissor_Lift"]'))).click()

    def minerScissLift(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="scrCan_we_use_Miner_s_Scissor_Lift"]'))).click()

    def crewSize(self, crw):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Crew_Size"]'))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Crew_Size"]'))).send_keys(crw)

    def estLaborHrs(self, hrs):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Est_Labor_Hrs_per_Crew_Member"]'))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Est_Labor_Hrs_per_Crew_Member"]'))).send_keys(hrs)

    def clickSave(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="slds-button slds-button_brand"]'))).click()







