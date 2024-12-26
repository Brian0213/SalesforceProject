from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CreateWorkOrderPage:

    def __init__(self, driver):
        self.driver = driver

    def clickFinishBtn(self):
        finbtn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Finish']")))
        self.driver.execute_script("arguments[0].click();", finbtn)

    def clickWorkOrderLk(self):
        finbtn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//slot[contains(text(),'00062829')]")))
        self.driver.execute_script("arguments[0].click();", finbtn)

    def ManWorkDetails(self):
        workdet=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Manage Work Details']")))
        self.driver.execute_script("arguments[0].click();", workdet)

    def WorkOID(self):
        addLitem=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='00191705']")))
        self.driver.execute_script("arguments[0].click();", addLitem)

    def AddLineItem(self):
        addLitem=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Line Item']")))
        self.driver.execute_script("arguments[0].click();", addLitem)

    def clickLabor(self, labor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='pw']"))).send_keys(labor)







