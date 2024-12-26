from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ProductFilterPage:

    def __init__(self, driver):
        self.driver = driver

    def PrdFamLabor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Labor']")
        shadow7.click()

    def PrdFamTravel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Travel']")
        shadow7.click()

    def PrdFamAEDPart(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='AED Part']")
        shadow7.click()

    def PrdFamDock(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Dock']")
        shadow7.click()

    def PrdFamDoor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Door']")
        shadow7.click()

    def PrdFamGate(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Gate']")
        shadow7.click()

    def PrdFamOperaElect(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Operator/Electrical']")
        shadow7.click()

    def PrdFamSpecialty(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Specialty']")
        shadow7.click()

    def PrdFamWaste(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Waste']")
        shadow7.click()

    def PrdFamExpense(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Expense']")
        shadow7.click()

    def PrdFamFieldSupp(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Field Supplies']")
        shadow7.click()

    def PrdFamFreight(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Freight']")
        shadow7.click()

    def PrdFamPermit(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Permitting']")
        shadow7.click()

    def PrdFamSafety(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Safety']")
        shadow7.click()

    def PrdFamSurvey(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Survey']")
        shadow7.click()

    def PrdFamBoomLft(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Boom Lift']")
        shadow7.click()

    def PrdFamFrklift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Forklift']")
        shadow7.click()

    def PrdFamMatLift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Material Lift']")
        shadow7.click()

    def PrdFamMISC(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous']")
        shadow7.click()

    def PrdFamScislift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002gA3IYAU.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Scissor Lift']")
        shadow7.click()














