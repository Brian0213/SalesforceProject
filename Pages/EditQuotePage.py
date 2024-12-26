from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class EditQuotePage:

    def __init__(self, driver):
        self.driver = driver

    def AddProdButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='sbPageContainer']"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Add Products']").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()
        #prodbtn=self.driver.execute_script('return document.querySelector("#sbPageContainer").shadowRoot.querySelector("#content > sb-line-editor").shadowRoot.querySelector("#actions > sb-custom-action:nth-child(1)").shadowRoot.querySelector("#mainButton")')
        #self.driver.execute_script("arguments[0].click();", prodbtn)
        # shadow0 = self.driver.find_element(By.CSS_SELECTOR, "[id='sbPageContainer']").shadow_root
        # time.sleep(3)
        # shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        # time.sleep(1)
        # shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Add Products']").shadow_root
        # time.sleep(1)
        # shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()


    def AddGroupButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='sbPageContainer']"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "[id='sbPageContainer']").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Add Group']").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()

    def UnGroupButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='sbPageContainer']"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "[id='sbPageContainer']").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Ungroup']").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()

    def QuickSaveButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='sbPageContainer']"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "[id='sbPageContainer']").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Quick Save']").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()

    def CalculateButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='sbPageContainer']"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "[id='sbPageContainer']").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Calculate]").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()

    def CancelButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='sbPageContainer']"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "[id='sbPageContainer']").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Cancel']").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()

    def SaveButton(self):
        shadow0 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "[id='sbPageContainer']").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "sb-custom-action[name='Save']").shadow_root
        shadow2.find_element(By.CSS_SELECTOR, "#mainButton").click()

    def OfferTypeExpense(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Expense']")
        shadow7.click()

    def OfferTypeFieldSupplies(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Field Supplies']")
        shadow7.click()

    def OfferTypeFreight(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Freight']")
        shadow7.click()

    def OfferTypeLabor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Labor']")
        shadow7.click()

    def OfferTypePart(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Part']")
        shadow7.click()

    def OfferTypePermit(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Permitting']")
        shadow7.click()

    def OfferTypePM(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='PM']")
        shadow7.click()

    def OfferTypeSafe(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Safety']")
        shadow7.click()

    def OfferTypeSubLabor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Sub Labor']")
        shadow7.click()

    def OfferTypeSurvey(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Survey']")
        shadow7.click()

    def OfferTypeTool(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#pf").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#panel").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "sb-filter-item[item='a2iDP000002g9VnYAI.value']").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "#field").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#picklist").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#myselect").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "[id='Tool']")
        shadow7.click()

    def ApplyButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "paper-drawer-panel:nth-child(12) > div:nth-child(2) > div:nth-child(1) > paper-button:nth-child(4)").click()

    def ClearFieldButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, '[id="clearfilter"]').click()

    def SelectButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "#plSelect").click()

    def SelAddMoreButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "#plSelectMore").click()

    def CancelButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "#plCancel").click()

    def FilterButton(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "#fb").click()

    def SearchProduct(self, searchitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(searchitem)

    def SearchProduct(self, searchitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(searchitem2)

    def SearchProduct(self, searchitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(searchitem3)

    def SearchCustom(self, customitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(customitem)

    def SearchCustom(self, customitem2):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(customitem2)

    def SearchCustom(self, customitem3):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(customitem3)

    def SearchTravel(self, travelitem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(travelitem)

    def SearchLabor(self, laboritem):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#headersearch").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#typeahead").shadow_root
        shadow3.find_element(By.CSS_SELECTOR, "#itemLabel").send_keys(laboritem)


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

    def QuanVal(self, value):
        shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(2) > sf-le-table-row:nth-child(1)").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > span:nth-child(1)")
        shadow8.send_keys(value)

    def DoorProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(2)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def DockProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(3)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def MHEProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(4)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def WasteProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(5)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def SpecialtyProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(6)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def GateProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(7)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ExpenseProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(8)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ScissorsProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(9)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def FoxliftProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(10)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def FieldSupplies(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(11)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def FreightProduct(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(12)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def LaborProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(13)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def TravelProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(14)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def GeneralHardware(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(15)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def PermittingProduct(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(16)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def SafteyProduct(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(17)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def SafeCheckProduct(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(18)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def BoomLiftProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(19)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def MaterialLiftProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(20)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ToolsMiscProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(21)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def OtherProducts(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-lookup[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#lookupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(3) > iron-list:nth-child(1) > sb-table-row:nth-child(22)").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def clickReconfigure(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, " div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(2) > sf-le-table-row:nth-child(1)").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, ".left-aligned").shadow_root
        shadow8.find_element(By.CSS_SELECTOR, "#actionButton1").click()

    def SupplierField(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, " div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(2) > sf-le-table-row:nth-child(1)").shadow_root
        shadow7.find_element(By.CSS_SELECTOR, " div:nth-child(7) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > span:nth-child(1)").click()

    def ReconFrieght(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "#row").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReconLabor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[label='Labor']").click()

    def ReconSubLabor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[role='tab'][label='Sub Labor']").click()

    def ReconTool(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[role='tab'][label='Tool']").click()

    def ReconTravel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[role='tab'][label='Travel']").click()

    def ReconExpense(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[role='tab'][label='Expense']").click()


    def ReLabManStand(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t1']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(1)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReconSaveBtn(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "#pcSave").click()

    def ReconCancelBtn(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow1.find_element(By.CSS_SELECTOR, "#pcCancel").click()

    def qleCostColumn(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "div.container.td.sf-le-table-cell.sf-le-table-row.focusable.right.editable.editMode.sf-has-focus").click()
        # shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1) > span:nth-child(1)").click()

    def qleCostColumn1(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(2) > sf-le-table-row:nth-child(1)").shadow_root
        shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1) > span:nth-child(1)").send_keys(230)
        # shadow6.find_element(By.CSS_SELECTOR, "#list > iron-list > div:nth-child(4) > sf-le-table-row").click()
        # shadow7.find_element("#content > div > div.container.td.sf-le-table-cell.sf-le-table-row.focusable.right.editable.editMode.sf-has-focus").click()



