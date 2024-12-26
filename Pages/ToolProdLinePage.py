from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ToolProdLinePage:

    def __init__(self, driver):
        self.driver = driver

    def ToolUnitedBoomLift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='United Rentals']")
        shadow7.click()

    def ToolUnitedForkLift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='United Rentals']")
        shadow7.click()

    def ToolUnitedMaterialLift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='United Rentals']")
        shadow7.click()

    def ToolUnitedMiscellaneous(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='United Rentals']")
        shadow7.click()

    def ToolUnitedScissorLift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='United Rentals']")
        shadow7.click()