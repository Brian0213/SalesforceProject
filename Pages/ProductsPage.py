from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def clickProductsBtn(self):
        prodpage_btn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Select a List View: Products']")))
        self.driver.execute_script("arguments[0].click();", prodpage_btn)

    def clickAllProductsTab(self):
        allprod_page=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class=' virtualAutocompleteOptionText'][normalize-space()='All Products']")))
        self.driver.execute_script("arguments[0].click();", allprod_page)

    def clickIntegratedProdTab(self):
        inteprod_page=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class=' virtualAutocompleteOptionText'][normalize-space()='Integrated Products']")))
        self.driver.execute_script("arguments[0].click();", inteprod_page)

    def clickProdMissTab(self):
        inteprod_page=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Products Missing Line or Activity Type']")))
        self.driver.execute_script("arguments[0].click();", inteprod_page)

    def RecentlyViewedTab(self):
        recview_page=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='virtualAutocompleteOptionText'][normalize-space()='Recently Viewed']")))
        self.driver.execute_script("arguments[0].click();", recview_page)

    def StockableProductsTab(self):
        stockprod_page=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Stockable Products']")))
        self.driver.execute_script("arguments[0].click();", stockprod_page)

