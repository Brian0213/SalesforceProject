from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class LocationPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def clickaddLocBtn(self):
        location_btn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Location']")))
        self.driver.execute_script("arguments[0].click();",location_btn)

    def clickAccountTab(self):
        account_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Accounts']")))
        self.driver.execute_script("arguments[0].click();", account_tab)

    def clickAccountName(self):
        account_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Meggitt (rockmart) Inc']")))
        self.driver.execute_script("arguments[0].click();", account_name)

    def locationName(self, locationID):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Location_Name"]'))).send_keys(locationID)

    def relationshipType(self, relation):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Relationship_Type"]'))).send_keys(relation)

    def relationTypePropM(self):
        rel= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Relationship_Type"]'))))
        rel.select_by_visible_text("Property Manager")

    def relationTypeTN(self):
        rel= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Relationship_Type"]'))))
        rel.select_by_visible_text("Tenant")

    def relationTypeGC(self):
        rel= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Relationship_Type"]'))))
        rel.select_by_visible_text("General Contractor")

    def relationTypeBO(self):
        rel= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Relationship_Type"]'))))
        rel.select_by_visible_text("Building Owner")

    def relationshiptype(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Relationship_Type"]'))).click()

    def relationshipType1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Relationship_Type"]'))).send_keys(Keys.ARROW_DOWN)

    def relationshipType2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Relationship_Type"]'))).send_keys(Keys.RETURN)

    def addressType(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Address_Type"]'))).click()

    def addressTypeLatLong(self):
        rel= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Address_Type"]'))))
        rel.select_by_visible_text("Latitude/Longitude")

    def addressType1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Address_Type"]'))).send_keys(Keys.ARROW_DOWN)

    def addressType2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Address_Type"]'))).send_keys(Keys.RETURN)

    def address(self, address_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search for Address..."]'))).send_keys(address_name)

    def addressC(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search for Address..."]'))).click()

    def address1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-p-horizontal_x-small slds-p-vertical_xx-small"]'))).click()

    def address2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search for Address..."]'))).send_keys(Keys.TAB)

    def address22(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search for Address..."]'))).send_keys(Keys.ARROW_DOWN)

    def address23(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search for Address..."]'))).send_keys(Keys.ARROW_DOWN)

    def address3(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search for Address..."]'))).send_keys(Keys.RETURN)

    def address4(self):
        self.action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def contactName(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).click()

    def contactNameScr(self):
        field=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)

    def contactName1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.ARROW_DOWN)

    def contactName2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.RETURN)

    def contactCheckbox(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper-body"]/div[2]/div/article/flowruntime-flow/flowruntime-lwc-body/div/flowruntime-list-container/div/flowruntime-base-section/div/flowruntime-screen-field[9]/flowruntime-lwc-field/div/flowruntime-flow-screen-input/flowruntime-input-wrapper2/div/lightning-input/lightning-primitive-input-checkbox/div/span/label/span[1]'))).click()

    def contactRelationship(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))).click()

    def contactRelationship1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))).send_keys(Keys.ARROW_DOWN)

    def contactRelationship2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))).send_keys(Keys.ENTER)

    def contactRelationshipPM(self):
        prod= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))))
        prod.select_by_visible_text("Purchasing Manager")

    def contactRelationshipSCSales(self):
        prod= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))))
        prod.select_by_visible_text("Site Contact - Sales")

    def contactRelationshipSCService(self):
        prod= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))))
        prod.select_by_visible_text("Site Contact - Service")

    def contactRelationshipAP(self):
        prod= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))))
        prod.select_by_visible_text("Accounts Payable")

    def contactRelationshipAR(self):
        prod= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))))
        prod.select_by_visible_text("Accounts receivable")

    def contactRelationshipEsm(self):
        prod= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))))
        prod.select_by_visible_text("Estimator")

    def contactRelationshipPRM(self):
        prod= Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="Contact_Relationship"]'))))
        prod.select_by_visible_text("Project Manager")

    def locationSuccess(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper-body"]/div[2]/div/article/flowruntime-flow/flowruntime-navigation-bar/footer/div[2]/lightning-button/button'))).click()

    def primaryP(self):
        self.action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()




