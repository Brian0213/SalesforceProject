from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class LaborTravelPage:

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

    def SearchLabor(self, laboritem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem)

    def SearchLabor(self, laboritem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem1)

    def SearchLabor(self, laboritem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem2)

    def SearchLabor(self, laboritem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem3)

    def SearchLabor(self, laboritem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem4)

    def SearchLabor(self, laboritem5):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem5)

    def SearchLabor(self, laboritem6):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem6)

    def SearchLabor(self, laboritem7):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem7)

    def SearchTravel(self, travelitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem)

    def SearchTravel(self, travelitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem1)

    def SearchTravel(self, travelitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem2)

    def SearchTravel(self, travelitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem3)

    def SearchTravel(self, travelitem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem4)

    def SearchTravel(self, travelitem5):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem5)

    def SearchTravel(self, travelitem6):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem6)

    def SearchTravel(self, travelitem7):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem7)

    def doorProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(2)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()
        # shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Expense']")
        # shadow7.click()

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