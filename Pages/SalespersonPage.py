from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

class SalespersonPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def clickAppLauncher(self):
        app_launch=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="slds-button slds-context-bar__button slds-icon-waffle_container slds-show"]')))
        self.driver.execute_script("arguments[0].click();", app_launch)