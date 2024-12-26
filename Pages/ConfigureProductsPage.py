from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ConfigureProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def clickReconfigureRow1(self):
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

    def clickReconfigureRow2(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(4) > sf-le-table-row:nth-child(1)").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, ".left-aligned").shadow_root
        shadow8.find_element(By.CSS_SELECTOR, "#actionButton1").click()

    def clickCloneLineBtn(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(2) > sf-le-table-row:nth-child(1)").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, ".left-aligned").shadow_root
        shadow8.find_element(By.CSS_SELECTOR, "#actionButton2").click()

    def clickDeleteBtn(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(2) > sf-le-table-row:nth-child(1)").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, ".left-aligned").shadow_root
        shadow8.find_element(By.CSS_SELECTOR, "#actionButton3").click()

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

    def ReLabManOverT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t1']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(3)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReLabManDoubleT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t1']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(5)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReLabManEmergencyT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t1']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(7)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReAddManDoubleT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t1']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(9)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReAddManOverT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t1']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(11)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReAddManStandardT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t1']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(13)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReAddManEmergencyT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t1']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(15)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReconSubLabor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[role='tab'][label='Sub Labor']").click()

    def ReSubLDockBumpers(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(5)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockLevel90TransPlate(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(7)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockLevBumpRemov(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(9)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockEODEODRemove(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(11)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockEODMechanical(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(13)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockPitAirHydraulic(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(17)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockPitGrdScissorTab(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(21)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockPitMechanical(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(23)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDocklights(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(29)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockSeal(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(31)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockSealMetalBuild(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(33)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockShelTruckCollaps(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(41)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockShelTruckRigid(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(43)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockMasterControlPanel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(45)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockTrackGuardsEA(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(47)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockTruckResMan(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(49)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockResManualwithAutoLights(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(51)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockTruckResPushBtn(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(53)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockTruckResStandOff(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(57)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorCoilSteelOP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(59)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorCoilingSteel100SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(61)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorCoilingSteel196SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(63)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorCoilingSteelSafetyEdge(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(67)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorHighSpeedSEL1400100SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(75)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorHighSpeedSEL1400196SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(77)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorHighSpeedSEL1400400SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(79)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorHighSpeedTermStart100SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(81)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorHighSpeedTermStart196SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(83)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorHighSpeedTermStart400SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(85)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollingSteelFireDoor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(87)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDockEODAirHydrauL(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(89)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteelInsula120SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(91)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteelInsula224SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(93)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteelInsula468SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(95)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteelInsula64SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(97)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteelMotorOP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(99)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteel120SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(101)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteel224SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(103)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteel468SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(105)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteel64SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(107)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorRollSteelPhotoEyes(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(109)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectDoubleShaft(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(113)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectFullView(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(115)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectHighLift(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(117)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectKnockoutDoor(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(119)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectOPJackshaft(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(121)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectOPTrolley(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(123)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSect120SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(125)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSect168SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(127)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSect224SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(129)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSect468SQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(131)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectOR64SQFTSQFT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(133)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectRemovOld(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(135)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLDoorSectSafeEdgeInstall(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(137)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSubLSpecialtyHvlsFan(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t2']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(139)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReconTool(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[role='tab'][label='Tool']").click()

    def ReBoom33ArticulatingDC(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, " div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(1)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom39ArticulatingDC(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(3)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom50Articulating(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(5)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom50Telescopic4WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(7)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom44Telescopic(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(9)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom42ArticulatingElectric(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(11)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom46ArticulatingElectric(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(13)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom64Articulating(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(15)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom64ArticulatingElectric(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(17)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom64ArticulElecMultiPower(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(19)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom64Telescopic(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(21)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom70Telescopic(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(23)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom85Articulating(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(25)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom80Telescopic(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(27)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom120Telescopic4WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(29)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift26Electric36Wide(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(33)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift26Electric68Wide(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(35)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift27Electric4WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(37)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift27IC4WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(39)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift33Electric32Wide(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(41)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift35Electric48Wide(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(43)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift35IC4WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(45)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift40Electric(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(47)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift40Electric4WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(49)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScissorLift49IC4WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(51)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftWHSE4000Electric(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(53)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftWHSE5000GasLP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(55)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftWHSE5000Electric(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(57)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftWHSE5000LowProfileGasLP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(59)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftWHSE6000GasLP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(61)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftWHSE8000GasLP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(63)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftVarReach450015UP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(65)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftVarReach500020(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(67)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftVarReach600034(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(69)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftVarReach600039(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(71)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftVarReach600049(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(73)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftVarReach800049(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(75)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftVarReach1000050UP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(77)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReForkLiftVarReach1200053UP(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(79)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReLiftMat400Manual(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(81)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReLiftMat15400Manual(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(81)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReLiftMat18650Manual(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(83)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReLiftMat25650Manual(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(85)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReCoreDrillStand(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(87)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReScrubberFloorRideonPropane(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(89)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReRideonScrubberElectric(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(91)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSweeperScrubberRideon(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(93)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReDrumFan(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(95)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReVertLift20SelfPropelled(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(97)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSawConcrete17HPSelfPropelled(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(99)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSawConcrete19HPSelfPropelled(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(101)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBladDiamond18WetAsphaltGreenConc(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(103)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSweeperRideOnPickup(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(107)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBackhoeLoader90HP2WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(109)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBackhoeLoader90HP4WD(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(111)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBackhoeBreaker(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(113)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSkidSteelLoader850(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(115)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSkidSteerAugerExtenstion(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(117)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSkidSteekTrackLoader2399(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(119)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSkidSteerLoader1899(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(121)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReTrailerFlatbed20(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(123)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReTrailerFlatbed40(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(125)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReTrailerEquipment14To8DrpTNDM(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(127)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReWelderArc500AmpDSLOrGAS(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(129)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReBoom50Articulating(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t3']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(131)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReconTravel(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[role='tab'][label='Travel']").click()

    def ReManOverTime(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t4']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(3)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReManEmergencyTT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t4']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(5)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReManDoubleTTR(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t4']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(7)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReAddManStandardT(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t4']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(9)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReAddManOverTimeTR(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t4']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(11)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReAddManDoubleTimeTR(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t4']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(13)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReAddManEmergencyTR(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t4']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(15)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReconExpense(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow4.find_element(By.CSS_SELECTOR, "paper-tab[role='tab'][label='Expense']").click()

    def ReEXP001(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t5']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "#row").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()

    def ReSurcharge(self):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-product-config[class='--desktop']").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#bundles").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#features").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-product-feature-list[name='t5']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "#ot").shadow_root
        shadow8 = shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div:nth-child(2) > sb-table-row:nth-child(3)").shadow_root
        shadow9 = shadow8.find_element(By.CSS_SELECTOR, "#selection").shadow_root
        shadow10 = shadow9.find_element(By.CSS_SELECTOR, "sb-table-cell-select[class='--desktop']").shadow_root
        shadow11 = shadow10.find_element(By.CSS_SELECTOR, "#checkbox").shadow_root
        shadow11.find_element(By.CSS_SELECTOR, "#checkboxContainer").click()





































