from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def clickAccountsTab(self):
        acct_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Accounts']")))
        self.driver.execute_script("arguments[0].click();", acct_tab)

    def clickOpportunityTab(self):
        oppor_tab=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Opportunities']")))
        self.driver.execute_script("arguments[0].click();", oppor_tab)

    def clickCpqQuoteTab(self):
        qte_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='CPQ Quotes']")))
        self.driver.execute_script("arguments[0].click();", qte_tab)

    def clickProductsTab(self):
        prod_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Products']")))
        self.driver.execute_script("arguments[0].click();", prod_tab)

    def clickProdRulTab(self):
        prorul_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Product Rules']")))
        self.driver.execute_script("arguments[0].click();", prorul_tab)

    def clickReportsTab(self):
        rep_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Reports']")))
        self.driver.execute_script("arguments[0].click();", rep_tab)

    def clickDashboardTab(self):
        dash_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Dashboards']")))
        self.driver.execute_script("arguments[0].click();", dash_tab)

    def clickPriceRulesTab(self):
        prcrul_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Price Rules']")))
        self.driver.execute_script("arguments[0].click();", prcrul_tab)

    def clickMoreBtn(self):
        more_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='More']")))
        self.driver.execute_script("arguments[0].click();", more_btn)

    def clickRatesTab(self):
        rate_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Rates')]")))
        self.driver.execute_script("arguments[0].click();", rate_tab)

    def clickSalesProgramTab(self):
        salpro_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Sales Programs')]")))
        self.driver.execute_script("arguments[0].click();", salpro_tab)

    def clickProdCstMarkTab(self):
        procstmrk_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Products Cost Markup')]")))
        self.driver.execute_script("arguments[0].click();", procstmrk_tab)

    def clickPrcActTab(self):
        prcarc_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Price Actions')]")))
        self.driver.execute_script("arguments[0].click();",prcarc_tab)

    def clickContPrcTab(self):
        contprc_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Contracted Prices')]")))
        self.driver.execute_script("arguments[0].click();", contprc_tab)

    def clickSuppPrcTab(self):
        supprc_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Supplier Pricing')]")))
        self.driver.execute_script("arguments[0].click();", supprc_tab)

    def clickCustPrtTab(self):
        custprt_tab= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Custom Parts Margin')]")))
        self.driver.execute_script("arguments[0].click();", custprt_tab)