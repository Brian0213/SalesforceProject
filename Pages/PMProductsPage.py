from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class PMProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def AddProdButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='sbPageContainer']"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Add Products']").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()

    def ApplyButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "paper-drawer-panel:nth-child(12) > div:nth-child(2) > div:nth-child(1) > paper-button:nth-child(4)").click()

    def SearchButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#search").click()

    def ProductCheckbox(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(3)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def SaveButton(self):
        shadow0 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "[id='sbPageContainer']").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Save']").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()

    def SelectButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "#plSelect").click()

    def SearchTravel(self, travelitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem)

    def SearchDock(self, dockitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem)

    def SearchDock(self, dockitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem1)

    def SearchDock(self, dockitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem2)

    def SearchDock(self, dockitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem3)

    def SearchDock(self, dockitem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem4)

    def SearchDock(self, dockitem5):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem5)

    def SearchDock(self, dockitem6):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem6)

    def SearchDock(self, dockitem7):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem7)

    def SearchDock(self, dockitem8):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem8)

    def SearchDock(self, dockitem9):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem9)

    def SearchDock(self, dockitem10):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem10)

    def SearchDock(self, dockitem11):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem11)

    def SearchDock(self, dockitem12):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dockitem12)

    def SearchDoor(self, dooritem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem)

    def SearchDoor(self, dooritem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem1)

    def SearchDoor(self, dooritem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem2)

    def SearchDoor(self, dooritem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem3)

    def SearchDoor(self, dooritem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem4)

    def SearchDoor(self, dooritem5):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem5)

    def SearchDoor(self, dooritem6):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem6)

    def SearchDoor(self, dooritem7):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem7)

    def SearchDoor(self, dooritem8):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem8)

    def SearchDoor(self, dooritem9):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem9)

    def SearchDoor(self, dooritem10):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem10)

    def SearchDoor(self, dooritem11):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem11)

    def SearchDoor(self, dooritem12):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem12)

    def SearchDoor(self, dooritem13):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem13)

    def SearchDoor(self, dooritem14):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem14)

    def SearchDoor(self, dooritem15):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem15)

    def SearchDoor(self, dooritem16):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem16)

    def SearchDoor(self, dooritem17):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem17)

    def SearchDoor(self, dooritem18):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem18)

    def SearchDoor(self, dooritem19):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem19)

    def SearchDoor(self, dooritem20):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem20)

    def SearchDoor(self, dooritem21):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem21)

    def SearchDoor(self, dooritem22):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem22)

    def SearchDoor(self, dooritem23):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem23)

    def SearchDoor(self, dooritem24):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem24)

    def SearchDoor(self, dooritem25):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem25)

    def SearchDoor(self, dooritem26):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem26)

    def SearchDoor(self, dooritem27):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem27)

    def SearchDoor(self, dooritem28):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(dooritem28)

    def SearchGate(self, gateitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(gateitem)

    def SearchGate(self, gateitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(gateitem1)

    def SearchGate(self, gateitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(gateitem2)

    def SearchGate(self, gateitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(gateitem3)

    def SearchGate(self, gateitem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(gateitem4)

    def SearchSpecial(self, specialty):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(specialty)

    def SearchWaste(self, wasteitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(wasteitem)

    def SearchWaste(self, wasteitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(wasteitem1)

    def SearchWaste(self, wasteitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(wasteitem2)

    def SearchWaste(self, wasteitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(wasteitem3)

    def SearchWaste(self, wasteitem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(wasteitem4)

    def SearchMaterial(self, materialitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(materialitem)

    def SearchMaterial(self, materialitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(materialitem1)

    def SearchMaterial(self, materialitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(materialitem2)

