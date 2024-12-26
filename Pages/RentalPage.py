from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class RentalPage:

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

    def SearchRental(self, boomitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem)

    def SearchRental(self, boomitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem1)

    def SearchRental(self, boomitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem2)

    def SearchRental(self, boomitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem3)

    def SearchRental(self, boomitem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem4)

    def SearchRental(self, boomitem5):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem5)

    def SearchRental(self, boomitem6):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem6)

    def SearchRental(self, boomitem7):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem7)

    def SearchRental(self, boomitem8):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem8)

    def SearchRental(self, boomitem9):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem9)

    def SearchRental(self, boomitem10):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem10)

    def SearchRental(self, boomitem11):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem11)

    def SearchRental(self, boomitem12):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem12)

    def SearchRental(self, boomitem13):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem13)

    def SearchRental(self, boomitem14):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem14)

    def SearchRental(self, boomitem15):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(boomitem15)

    def SearchScissor(self, scissoritem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem)

    def SearchScissor(self, scissoritem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem1)

    def SearchScissor(self, scissoritem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem2)

    def SearchScissor(self, scissoritem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem3)

    def SearchScissor(self, scissoritem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem4)

    def SearchScissor(self, scissoritem5):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem5)

    def SearchScissor(self, scissoritem6):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem6)

    def SearchScissor(self, scissoritem7):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem7)

    def SearchScissor(self, scissoritem8):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem8)

    def SearchScissor(self, scissoritem9):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem9)

    def SearchScissor(self, scissoritem10):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem10)

    def SearchScissor(self, scissoritem11):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(scissoritem11)

    def SearchFork(self, forkitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem)

    def SearchFork(self, forkitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem1)

    def SearchFork(self, forkitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem2)

    def SearchFork(self, forkitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem3)

    def SearchFork(self, forkitem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem4)

    def SearchFork(self, forkitem5):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem5)

    def SearchFork(self, forkitem6):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem6)

    def SearchFork(self, forkitem7):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem7)

    def SearchFork(self, forkitem8):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem8)

    def SearchFork(self, forkitem9):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem9)

    def SearchFork(self, forkitem10):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem10)

    def SearchFork(self, forkitem11):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem11)

    def SearchFork(self, forkitem12):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem12)

    def SearchFork(self, forkitem13):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(forkitem13)

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

    def SearchMaterial(self, materiaitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(materiaitem)

    def SearchMaterial(self, materiaitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(materiaitem1)

    def SearchMaterial(self, materiaitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(materiaitem2)

    def SearchOther(self, otheritem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(otheritem)

    def SearchOther(self, otheritem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(otheritem1)

    def SearchOther(self, otheritem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(otheritem2)

    def SearchToolsMISC(self, toolsitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem)

    def SearchToolsMISC(self, toolsitem1):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem1)

    def SearchToolsMISC(self, toolsitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem2)

    def SearchToolsMISC(self, toolsitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem3)

    def SearchToolsMISC(self, toolsitem4):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem4)

    def SearchToolsMISC(self, toolsitem5):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem5)

    def SearchToolsMISC(self, toolsitem6):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem6)

    def SearchToolsMISC(self, toolsitem7):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem7)

    def SearchToolsMISC(self, toolsitem8):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem8)

    def SearchToolsMISC(self, toolsitem9):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem9)

    def SearchToolsMISC(self, toolsitem10):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem10)

    def SearchToolsMISC(self, toolsitem11):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem11)

    def SearchToolsMISC(self, toolsitem12):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem12)

    def SearchToolsMISC(self, toolsitem13):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem13)

    def SearchToolsMISC(self, toolsitem14):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem14)

    def SearchToolsMISC(self, toolsitem15):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem15)

    def SearchToolsMISC(self, toolsitem16):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem16)

    def SearchToolsMISC(self, toolsitem17):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem17)

    def SearchToolsMISC(self, toolsitem18):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem18)

    def SearchToolsMISC(self, toolsitem19):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem19)

    def SearchToolsMISC(self, toolsitem20):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem20)

    def SearchToolsMISC(self, toolsitem21):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(toolsitem21)





