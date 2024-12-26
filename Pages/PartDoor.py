from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PartDoorPage:

    def __init__(self, driver):
        self.driver = driver

    def M1001001(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(28)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def M1031054(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(4)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def M1031055(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(5)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def M1031095(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(5)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()
