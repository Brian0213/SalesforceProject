from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class ServiceCoordinatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def lkServiceCoord(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Search"]'))).send_keys("Service Coordinator User")

    def clickServiceCoord(self):
        self.action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def userDetailBtn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='User Detail']"))).click()

    def clickSCLogBtn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//td[@id='topButtonRow']//input[@title='Login']"))).click()

    def clickMenuNav(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Show Navigation Menu']//lightning-primitive-icon[@variant='bare']"))).click()

    def pickAccounts(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Accounts')]"))).click()

    def pickLocations(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Locations')]"))).click()

    def pickOpportunities(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Opportunities')]"))).click()

    def pickWorkOrders(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Work Orders')]"))).click()

    def pickCPQQuotes(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'CPQ Quotes')]"))).click()

    def pickPMPlan(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Maintenance Plans')]"))).click()

    def pickServAppoint(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Service Appointments')]"))).click()

    def clickHome(self):
        account_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Home']")))
        self.driver.execute_script("arguments[0].click();", account_tab)

    def clickWaffle(self):
        waffle_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='slds-icon-waffle']")))
        self.driver.execute_script("arguments[0].click();", waffle_tab)

    def srhMinerService(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search apps and items..."]'))).send_keys("Miner Service Console")
    def reMiner(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search apps and items..."]'))).send_keys(Keys.ENTER)

    def newServiceWO(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='New Service Work Order']"))).click()

    def customerAcct(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[name="Account_Type-7522"]'))).click()

