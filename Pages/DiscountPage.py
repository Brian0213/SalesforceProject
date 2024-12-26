from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class DiscountPage:

    def __init__(self, driver):
        self.driver = driver

    def addTwenty(self, field):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(2) > sf-le-table-row:nth-child(1)").click()
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(1) > div:nth-child(9) > div:nth-child(1) > span:nth-child(1)")
        shadow7.send_keys(field)

    def addTwit(self, field):
        shadow0 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sbPageContainer"))).shadow_root
        #shadow0 = self.driver.find_element(By.CSS_SELECTOR, "#sbPageContainer").shadow_root
        shadow1 = shadow0.find_element(By.CSS_SELECTOR, "sb-line-editor[class='--desktop").shadow_root
        shadow2 = shadow1.find_element(By.CSS_SELECTOR, "#groupLayout").shadow_root
        shadow3 = shadow2.find_element(By.CSS_SELECTOR, "#Group_").shadow_root
        shadow4 = shadow3.find_element(By.CSS_SELECTOR, "#groupTabs").shadow_root
        shadow5 = shadow4.find_element(By.CSS_SELECTOR, "sb-group-tabs[name='t0']").shadow_root
        shadow6 = shadow5.find_element(By.CSS_SELECTOR, ".largeQuote.--desktop").shadow_root
        shadow7 = shadow6.find_element(By.CSS_SELECTOR, "div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > iron-list:nth-child(2) > div:nth-child(2) > sf-le-table-row:nth-child(1)").shadow_root
        shadow7.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(1) > div:nth-child(9) > div:nth-child(1) > span:nth-child(1)").send_keys(field)

