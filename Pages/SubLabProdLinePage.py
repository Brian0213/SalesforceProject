from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class SubLabProdLinePage:

    def __init__(self, driver):
        self.driver = driver

    def SuLbDockAirBDoLev(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Airbag Dock Leveler']")
        shadow7.click()

    def SuLbDockBumper(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Bumper']")
        shadow7.click()

    def SuLbDockLight(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Dock Lights']")
        shadow7.click()

    def SuLbDockRampRail(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Dock Ramp Rails']")
        shadow7.click()

    def SuLbDockSeal(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Dock Seal']")
        shadow7.click()

    def SuLbDockShelter(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Airbag Dock Shelter']")
        shadow7.click()

    def SuLbDockDrOps(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Door Operators']")
        shadow7.click()

    def SuLbDockEdgeHydra(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Edge of Dock Leveler (Hydraulic)']")
        shadow7.click()

    def SuLbDockEdgeMech(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Edge of Dock Leveler (Mechanical)']")
        shadow7.click()

    def SuLbDockHydraLvler(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Hydraulic Dock Leveler']")
        shadow7.click()

    def SuLbDockMechLvler(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Mechanical Dock Leveler']")
        shadow7.click()

    def SuLbDockMultiVertLift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Multi-story Vertical Lift']")
        shadow7.click()

    def SuLbDockPneuLvler(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Pneumatic Dock Leveler']")
        shadow7.click()

    def SuLbDockRailCLvler(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Railcar Dock Leveler']")
        shadow7.click()

    def SuLbDockScissorLift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Scissor Lift']")
        shadow7.click()

    def SuLbDockTrailRest(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Trailer Restraint']")
        shadow7.click()

    def SuLbDockUniversal(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Universal Dock']")
        shadow7.click()

    def SuLbDockVertiLvler(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Vertical Dock Leveler']")
        shadow7.click()

    def SuLbDockWheelChock(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Wheel Chock']")
        shadow7.click()

    def SuLbDoorAirCurtain(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Air Curtain']")
        shadow7.click()

    def SuLbDoorAutoSlid(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Automatic Sliding Door']")
        shadow7.click()

    def SuLbDoorAutoSwing(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Automatic Swinging Door']")
        shadow7.click()

    def SuLbDoorBiFoldHang(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Bi-Fold Hangar Door']")
        shadow7.click()

    def SuLbDoorColdStor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cold Storage Door']")
        shadow7.click()

    def SuLbDoorCooler(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Cooler Door']")
        shadow7.click()

    def SuLbDoorOperators(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Door Operators']")
        shadow7.click()

    def SuLbDoorFire(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Fire Door']")
        shadow7.click()

    def SuLbDoorFldBarrier(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Flood Barrier']")
        shadow7.click()

    def SuLbDoorGlasAlum(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Glass Aluminum Door']")
        shadow7.click()

    def SuLbDoorHandiAcc(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Handicap Access Door']")
        shadow7.click()

    def SuLbDoorHerculite(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Herculite Door']")
        shadow7.click()

    def SuLbDoorHighSpeed(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='High Speed Door']")
        shadow7.click()

    def SuLbDoorHollMet(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Hollow Metal Door']")
        shadow7.click()

    def SuLbDoorImpact(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Impact Door']")
        shadow7.click()

    def SuLbDoorKnockOut(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Knock Out Door']")
        shadow7.click()

    def SuLbDoorPersPede(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Personnel or Pedestrian Door']")
        shadow7.click()

    def SuLbDoorRollAlumGri(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Rolling Aluminum Grille']")
        shadow7.click()

    def SuLbDoorRollSteellSheet(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Rolling Steel/Sheet Door Parts']")
        shadow7.click()

    def SuLbDoorRollHatch(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Roof Hatch']")
        shadow7.click()

    def SuLbDoorScissorGate(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Scissor Gate']")
        shadow7.click()

    def SuLbDoorSectional(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sectional Door']")
        shadow7.click()

    def SuLbDoorSectionalSect(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sectional Door Sections']")
        shadow7.click()

    def SuLbDoorSlidAlumGril(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sliding Aluminum Grille']")
        shadow7.click()

    def SuLbDoorSlidHang(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sliding Hangar Door']")
        shadow7.click()

    def SuLbDoorStorefront(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Storefront']")
        shadow7.click()

    def SuLbDoorStrip(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Strip Doors']")
        shadow7.click()

    def SuLbDoorUnivLvler(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Universal Dock Leveler']")
        shadow7.click()

    def SuLbDoorUniversal(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Universal Door']")
        shadow7.click()

    def SuLbDoorWood(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Wood Door']")
        shadow7.click()

    def SuLbDoorRolStlCoil(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Rolling Steel or Coiling Door']")
        shadow7.click()

    def SuLbDoorSheet(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sheet Door']")
        shadow7.click()

    def SuLbDoorSectionalAccess(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sectional Door Accessories']")
        shadow7.click()

    def SuLbDoorMiscSectionAccess(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Misc Sectional Door Sections']")
        shadow7.click()

    def SuLbDoorSectionalDrums(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sectional Door Drums']")
        shadow7.click()

    def SuLbDoorShaftTracks(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Shaft and Tracks']")
        shadow7.click()

    def SuLbDoorSectionalSect(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VmYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Seal for Doors']")
        shadow7.click()
