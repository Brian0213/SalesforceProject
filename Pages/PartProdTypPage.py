from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class PartProdTypPage:

    def __init__(self, driver):
        self.driver = driver

    def AedPedeDoorFullDoor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def AedPedeDoorSparePart(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def AedSenorsSparePart(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def AedStanleySparePart(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def AedUniversalSparePart(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockAirbagLevel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Leveler']")
        shadow7.click()

    def DockAirbagSparePart(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockBumperFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Bumper']")
        shadow7.click()

    def DockLightFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Light']")
        shadow7.click()

    def DockLightSparePrt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockRampRail(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Ramp Rail']")
        shadow7.click()

    def DockSealFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Seal']")
        shadow7.click()

    def DockSealSparPrt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockSheltFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Shelter']")
        shadow7.click()

    def DockSheltSparPrt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockOperBelt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Belts']")
        shadow7.click()

    def DockOperCrdRel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cords & Reels']")
        shadow7.click()

    def DockOperFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Operator']")
        shadow7.click()

    def DockOperLogBrd(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Logic Boards']")
        shadow7.click()

    def DockOperMiscElect(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous Electrical']")
        shadow7.click()

    def DockOperAccesso(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Operator Accessories']")
        shadow7.click()

    def DockOperPushbKeys(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Pushbuttons and Keyswitches']")
        shadow7.click()

    def DockOperRemotes(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Remotes']")
        shadow7.click()

    def DockOperSafeties(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Safeties']")
        shadow7.click()

    def DockOperTransfReceTransm(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Transformer/Receiver/Transmitter']")
        shadow7.click()

    def DockEdgeHydraLevFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Leveler']")
        shadow7.click()

    def DockEdgeHydraLevSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockEdgeMechLevFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Leveler']")
        shadow7.click()

    def DockEdgeMechLevSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockHydraLevFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Leveler']")
        shadow7.click()

    def DockHydraLevSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockMechLevFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Leveler']")
        shadow7.click()

    def DockMechLevSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockMultiSFullLft(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Lift']")
        shadow7.click()

    def DockMultiSSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockPneuMFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Leveler']")
        shadow7.click()

    def DockPneuMSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockRailCFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Leveler']")
        shadow7.click()

    def DockRailCSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockScissFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Lift']")
        shadow7.click()

    def DockScissFullLft(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Scissor Lift']")
        shadow7.click()

    def DockScissSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockTrailResFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Restraint']")
        shadow7.click()

    def DockTrailResSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockUniverSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockUniverDkSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Universal Dock Spare Part']")
        shadow7.click()

    def DockVertFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Dock Leveler']")
        shadow7.click()

    def DockVertSprP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DockWheelFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Wheel Chock']")
        shadow7.click()

    def DoorAirCurtFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Air Curtain']")
        shadow7.click()

    def DoorCurtFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Curtain']")
        shadow7.click()

    def DoorAirCurtSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorAutoSlidFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorAutoSlidSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorAutoSwingFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorAutoSwingSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorBiFHangFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorBiFHangSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorColdStorFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorColdStorSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorCoolerFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorCoolerSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorOpsBelt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Belts']")
        shadow7.click()

    def DoorOpsCrdRel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cords & Reels']")
        shadow7.click()

    def DoorOpsFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Operator']")
        shadow7.click()

    def DoorOpsLogBrd(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Logic Boards']")
        shadow7.click()

    def DoorOpsMiscElect(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous Electrical']")
        shadow7.click()

    def DoorOpsAccess(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Operator Accessories']")
        shadow7.click()

    def DoorOpsPushBKeyS(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Pushbuttons and Keyswitches']")
        shadow7.click()

    def DoorOpsRemote(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Remotes']")
        shadow7.click()

    def DoorOpsSafe(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Safeties']")
        shadow7.click()

    def DoorOpsTransfRecTransm(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Transformer/Receiver/Transmitter']")
        shadow7.click()

    def DoorFireFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorFireSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorFldBarrFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Barrier']")
        shadow7.click()

    def DoorFldBarrSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorGlsAlumFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorGlsAlumSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorHandiAccFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorHandiAccSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorHercuFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorHercuSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorHighSpdFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorHighSpdSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorHollMetFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorHollMetSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorImpactFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorImpactSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorKnockOFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorKnockOSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorPersPedeFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorPersPedeSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorRollAlumFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Grille']")
        shadow7.click()

    def DoorRollAlumSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorRoofHatchFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Hatch']")
        shadow7.click()

    def DoorRoofHatchSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorScisGatFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Gate']")
        shadow7.click()

    def DoorScisGatSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorSecBotSel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Bottom Seal']")
        shadow7.click()

    def DoorSecCabSet(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cable Set']")
        shadow7.click()

    def DoorSecDrum(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Drum']")
        shadow7.click()

    def DoorSecCabSet(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cable Set']")
        shadow7.click()

    def DoorSecFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorSecHinge(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Hinge']")
        shadow7.click()

    def DoorSecMiscHard(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous Hardware']")
        shadow7.click()

    def DoorSecMiscMetal(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous Metal']")
        shadow7.click()

    def DoorSecRoller(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Roller']")
        shadow7.click()

    def DoorSecDoorSec(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sectional Door Sections']")
        shadow7.click()

    def DoorSecShaft(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Shaft']")
        shadow7.click()

    def DoorSecSlidLck(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Slide Lock']")
        shadow7.click()

    def DoorSecSpareP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorSecStiles(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Stiles']")
        shadow7.click()

    def DoorSecStrut(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Strut']")
        shadow7.click()

    def DoorSecTrack(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Track']")
        shadow7.click()

    def DoorSecVinInsul(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Vinyl Insulation']")
        shadow7.click()

    def DoorSecSectBotSel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Bottom Seal']")
        shadow7.click()

    def DoorSecSectCabSet(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cable Set']")
        shadow7.click()

    def DoorSecSectDrum(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Drum']")
        shadow7.click()

    def DoorSecSectCabSet(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cable Set']")
        shadow7.click()

    def DoorSecSectFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorSecSectHinge(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Hinge']")
        shadow7.click()

    def DoorSecSectMiscHard(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous Hardware']")
        shadow7.click()


    def DoorSecSectRoller(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Roller']")
        shadow7.click()

    def DoorSecSectDoorSec(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sectional Door Sections']")
        shadow7.click()

    def DoorSecSectShaft(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Shaft']")
        shadow7.click()

    def DoorSecSectSlidLck(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Slide Lock']")
        shadow7.click()

    def DoorSecSectSpareP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorSecSectStiles(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Stiles']")
        shadow7.click()

    def DoorSecSectStrut(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Strut']")
        shadow7.click()

    def DoorSecSectTrack(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Track']")
        shadow7.click()

    def DoorSecSectVinInsul(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Vinyl Insulation']")
        shadow7.click()

    def DoorSlidAlumFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Grille']")
        shadow7.click()

    def DoorSlidAlumSpareP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorSlidHangFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorSlidHangSpareP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorStoreFFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Storefront']")
        shadow7.click()

    def DoorStoreFSpareP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorStripFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorStripSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorUnivDckLevel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sensors']")
        shadow7.click()

    def DoorUnivDckSpareP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorUnivBotSel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Bottom Seal']")
        shadow7.click()

    def DoorUnivSen(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sensors']")
        shadow7.click()

    def DoorUnivSpareP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorWoodFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorWoodSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorRolSCoilDSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorSheetF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Door']")
        shadow7.click()

    def DoorSecAccessSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorMiscSecAccessSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorSecDrumSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorShatTrkSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def DoorSealsFSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def GateAcceCtl(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Access Controls']")
        shadow7.click()

    def GateAcceSctlF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Access Controls']")
        shadow7.click()

    def GateAcceCtlSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def GateBarrArmF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Barrier Arm']")
        shadow7.click()

    def GateBarrArmSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def GateFencF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Fencing']")
        shadow7.click()

    def GateFencSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def GateOperBelt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Belts']")
        shadow7.click()

    def GateOperCrdRel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cords & Reels']")
        shadow7.click()

    def GateOperFull(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Operator']")
        shadow7.click()

    def GateOperLogBrd(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Logic Boards']")
        shadow7.click()

    def GateOperMiscElect(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous Electrical']")
        shadow7.click()

    def GateOperAccesso(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Operator Accessories']")
        shadow7.click()

    def GateOperOthPrt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Other Parts']")
        shadow7.click()

    def GateOperPushbKeys(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Pushbuttons and Keyswitches']")
        shadow7.click()

    def GateOperRemotes(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Remotes']")
        shadow7.click()

    def GateOperSafeties(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Safeties']")
        shadow7.click()

    def GateOperSparP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def GateOperTransfReceTransm(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Transformer/Receiver/Transmitter']")
        shadow7.click()

    def GateSparPrtACtl(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Access Controls']")
        shadow7.click()

    def GateSparPrtGHard(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Gate Hardware']")
        shadow7.click()

    def GateSparPMiscMet(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous Metal']")
        shadow7.click()

    def GateSparPVid(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def OperElecSparPrt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def OpElLogBrdSparPrt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def OpElMiscElect(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Miscellaneous Electrical']")
        shadow7.click()

    def OpEleSafeties(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Safeties']")
        shadow7.click()

    def OpElBelt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Belts']")
        shadow7.click()

    def OpElCrdRel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cords & Reels']")
        shadow7.click()

    def OpElOps(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def OpElOpsAccess(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def OpElPushBKeyS(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Pushbuttons and Keyswitches']")
        shadow7.click()

    def OpElRemote(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Remotes']")
        shadow7.click()

    def OpElTranRecTran(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Transformer/Receiver/Transmitter']")
        shadow7.click()

    def SpecAccessCntrl(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Access Controls']")
        shadow7.click()

    def SpecAirCurtF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Air Curtain']")
        shadow7.click()

    def SpecFulCurt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Curtain']")
        shadow7.click()

    def SpecAirCurt(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def SpecGudRalF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Guard Rails']")
        shadow7.click()

    def SpecGudRalSpaPr(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def SpecHvlsF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full HVLS Fan']")
        shadow7.click()

    def SpecHvlsSpaPr(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def SpecSafeRalF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Safety Rails']")
        shadow7.click()

    def SpecSafeRalSpaPr(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def WasteBalerF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Baler']")
        shadow7.click()

    def WasteBalerSpaPr(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def WasteConveyF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Conveyor']")
        shadow7.click()

    def WasteConveySpaPr(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def WasteLiftTabF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Lift Table']")
        shadow7.click()

    def WasteLiftTabSpaPr(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def WasteShredF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Shredder']")
        shadow7.click()

    def WasteShredSpaPr(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()

    def WasteTrashCompF(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Full Trash Compactor']")
        shadow7.click()

    def WasteTrashCompSpaPr(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9YyYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Spare Part']")
        shadow7.click()








