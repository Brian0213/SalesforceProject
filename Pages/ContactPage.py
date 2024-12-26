from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    def clickAccountTab(self):
        account_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Accounts']")))
        self.driver.execute_script("arguments[0].click();", account_tab)

    def clickAccountName(self):
        account_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Meggitt (rockmart) Inc']")))
        self.driver.execute_script("arguments[0].click();", account_name)

    def clickContactBtn(self):
        contact_btn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="Account.New_Contact_and_Relationship"]')))
        self.driver.execute_script("arguments[0].click();", contact_btn)

    def clickCreateNewContact(self):
        create_new=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Create New Contact')]")))
        self.driver.execute_script("arguments[0].click();", create_new)

    def clickChooseExistingContact(self):
        exist_contact=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Choose Existing Contact')]")))
        self.driver.execute_script("arguments[0].click();", exist_contact)

    def Salutation(self):
        salut=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Salutation - Current Selection: --None--"]')))
        self.driver.execute_script("arguments[0].click();", salut)

    def pickMr(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Mr.')]"))).click()

    def pickMs(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Ms.')]"))).click()

    def pickMrs(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Mrs.')]"))).click()

    def pickDr(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Dr.')]"))).click()

    def pickProf(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Prof.')]"))).click()

    def firstName(self, fname):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="firstName"]'))).send_keys(fname)

    def middleName(self, mname):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="middleName"]'))).send_keys(mname)

    def lastName(self, lname):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="lastName"]'))).send_keys(lname)

    def eMail(self, email):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Email"]'))).send_keys(email)

    def pHone(self, phone):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Phone"]'))).send_keys(phone)

    def mobilePhone(self, mobile):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="MobilePhone"]'))).send_keys(mobile)

    def tiTle(self, title):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="Title"]'))).send_keys(title)

    def addressCheckbox(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper-body"]/div[2]/div/article/flowruntime-flow/flowruntime-lwc-body/div/flowruntime-list-container/div/flowruntime-base-section/div/flowruntime-screen-field[10]/flowruntime-lwc-field/div/flowruntime-flow-screen-input/flowruntime-input-wrapper2/div/lightning-input/lightning-primitive-input-checkbox/div/span/label/span[1]'))).click()

    def addressCheck(self):
        add_check=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Salutation - Current Selection: --None--"]')))
        self.driver.execute_script("arguments[0].click();", add_check)

    def srcAddress(self, addy):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(addy)

    def clickNext(self):
        add_check=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper-body"]/div[2]/div/article/flowruntime-flow/flowruntime-navigation-bar/footer/div[2]/lightning-button/button')))
        self.driver.execute_script("arguments[0].click();", add_check)

    def acctPayable(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Accounts Payable')]"))).click()

    def acctReceivable(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Accounts Receivable')]"))).click()

    def Estimator(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Estimator')]"))).click()

    def projectManager(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Project Manager')]"))).click()

    def purchaseManager(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Purchasing Manager')]"))).click()

    def siteContSales(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Site contact Sales')]"))).click()

    def siteContService(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Site contact Service')]"))).click()

    def clickNext2(self):
        add_check=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper-body"]/div[2]/div/article/flowruntime-flow/flowruntime-navigation-bar/footer/div[2]/lightning-button[2]')))
        self.driver.execute_script("arguments[0].click();", add_check)

    def recInvoiceCheckbox(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Receives Invoice')]"))).click()

    def confirmContact(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper-body"]/div[2]/div/article/flowruntime-flow/flowruntime-navigation-bar/footer/div[2]/lightning-button/button'))).click()

    def Next(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="slds-button slds-button_icon slds-button_icon-container"]'))).click()

    def primaryContact1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.TAB)

    def primaryContact2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="slds-combobox__input slds-input"]'))).send_keys(Keys.RETURN)






