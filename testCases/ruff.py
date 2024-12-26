from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
act=ActionChains(driver)

driver.get("https://onpointgroup--opgsit.sandbox.my.salesforce.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("oluwasegun.ojeyinka@onpointgroup.com.opg.sit")
time.sleep(4)
driver.find_element(By.XPATH, "//input[@name='pw']").send_keys("Welcome@2026")
time.sleep(4)
# driver.find_element(By.XPATH, "//input[@name='Login']").click()

driver.find_element(By.XPATH, "//input[@id='Login']").click()
time.sleep(5)


# time.sleep(10)

# driver.find_element(By.XPATH, "//div[@class='profileTrigger branding-user-profile bgimg slds-avatar slds-avatar_profile-image-small circular forceEntityIcon']//span[@class='uiImage']").click()
# time.sleep(7)
# driver.find_element(By.XPATH, "//a[@class='profile-link-label'][normalize-space()='Oluwasegun Ojeyinka']").click()
# time.sleep(7)
# driver.find_element(By.XPATH, '//button[@aria-label="Search"]').send_keys("Service Coordinator User")
# time.sleep(5)
# act.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[@title='User Detail']").click()
# time.sleep(5)
# driver.switch_to.frame(0)
# time.sleep(5)
# driver.find_element(By.XPATH, "//td[@id='topButtonRow']//input[@title='Login']").click()

# driver.find_element(By.XPATH, '//a[href="/lightning/r/User/005DP000008cvngYAA/view"]').click()
# driver.find_element(By.XPATH, "//div[@class='slds-icon-waffle']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, '//input[@placeholder="Search apps and items..."]').send_keys("Miner Service Console")
# time.sleep(3)
# driver.find_element(By.XPATH, '//input[@placeholder="Search apps and items..."]').send_keys(Keys.ENTER)
# time.sleep(3)
# driver.find_element(By.XPATH, '//button[@class="slds-button slds-button_neutral search-button slds-truncate"]').send_keys("Service Coordinator User")
# time.sleep(10)
# driver.find_element(By.XPATH, '//a[@data-recordid="005DP000008ctaBYAQ"]').click()

# driver.find_element(By.XPATH, "//div[@class='slds-icon-waffle']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, '//input[@placeholder="Search apps and items..."]').send_keys("Miner Service Console")
# time.sleep(3)
# driver.find_element(By.XPATH, '//input[@placeholder="Search apps and items..."]').send_keys(Keys.ENTER)
# time.sleep(3)
# driver.find_element(By.XPATH, '//span[@class="uiImage"]').click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//span[contains(text(),'Oluwasegun Ojeyinka')]").click()
# driver.find_element(By.XPATH, '//div[@title="User Detail"]').click()
# # driver.find_element(By.XPATH, '//button[@aria-label="Search"]').send_keys("Service Coordinator User")
# time.sleep(3)
# time.sleep(3)
# driver.find_element(By.XPATH, '//input[@placeholder="Search Setup"]').send_keys(Keys.ARROW_DOWN)
# time.sleep(3)
# driver.find_element(By.XPATH, '//input[@placeholder="Search Setup"]').send_keys(Keys.ENTER)
# time.sleep(3)
# # driver.switch_to.parent_frame()
# # time.sleep(5)
# driver.find_element(By.XPATH, "//body[1]/div[4]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/section[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/a[1]").click()
# # innerframe=driver.find_element(By.XPATH, '//iframe[@title="User: Service Coordinator User ~ Salesforce - Performance Edition"]')
# # driver.switch_to.frame(innerframe)
# time.sleep(5)
# # driver.find_element(By.XPATH, "//td[@id='topButtonRow']//input[@title='Login']").click()
time.sleep(10)
# qte_tab=driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='CPQ Quotes']")
# driver.execute_script("arguments[0].click();", qte_tab)
# time.sleep(5)
# quoteid = driver.find_element(By.XPATH, "//a[contains(text(),'Q-03800')]")
# driver.execute_script("arguments[0].click(true);", quoteid)
# time.sleep(5)
# crO=driver.find_element(By.XPATH, "//button[contains(text(),'Create Work Order')]")
# driver.execute_script("arguments[0].click(true);", crO)
# time.sleep(5)
# windowsIDs = driver.window_handles
# parentwindowid = windowsIDs[0]
# print(parentwindowid)
# time.sleep(3)
# driver.switch_to.window(parentwindowid)
# time.sleep(5)
# finish=driver.find_element(By.XPATH, "//button[normalize-space()='Finish']")
# driver.execute_script("arguments[0].click();", finish)


# wo=driver.find_element(By.XPATH, "//li[4]//lst-related-list-quick-link[1]//div[1]//div[1]//records-hoverable-link[1]//div[1]//a[1]//slot[1]//span[1]")
# driver.execute_script("arguments[0].click(true);", wo)
# time.sleep(5)
# wono=driver.find_element(By.XPATH, "//a[@title='00191563']")
# driver.execute_script("arguments[0].click(true);", wono)
# time.sleep(5)
# MWD=driver.find_element(By.XPATH, "//span[normalize-space()='Manage Work Details']")
# driver.execute_script("arguments[0].click(true);", MWD)
# time.sleep(5)
# MWDlineitem=driver.find_element(By.XPATH, "//button[normalize-space()='Add Line Item']")
# driver.execute_script("arguments[0].click(true);", MWDlineitem)
# time.sleep(5)
# # time.sleep(10)
# driver.switch_to.frame(1)
# dropdown = driver.find_element(By.XPATH, "//select[@id='select-2474']")
#
# select = Select(dropdown)
#
# select.select_by_value("Expenses")
# driver.find_element(By.XPATH, "//div[@class='lookup-overlay opened']").click()
# windowsIDs = driver.window_handles
# parentwindowid = windowsIDs[0]
# time.sleep(3)
# driver.switch_to.window(parentwindowid)
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, "#select-2474 > option:nth-child(2)")

#driver.find_element(By.XPATH, '//*[@id="select-2474"]/option[3]').click()

# driver.execute_script("window.scrollBy(0, 2230)")
# time.sleep(5)

# scroll=driver.find_element(By.XPATH, "//article[@aria-label='Approvals']//span[@class='view-all-label']")
# view=driver.execute_script("arguments[0].scrollIntoView();", scroll)
# view.click()
#
# approveviewall=driver.find_element(By.XPATH, "//article[@aria-label='Approvals']//span[@class='view-all-label']")
# driver.execute_script("arguments[0].click(true);", approveviewall)
# time.sleep(5)

# driver.switch_to.frame(1)
# time.sleep(5)
#
# approvalid=driver.find_element(By.XPATH, '//*[@id="brandBand_2"]/div/div/div[2]/div/lst-related-list-desktop/article/lst-related-list-view-manager/lst-common-list-internal/div/div/lst-primary-display-manager/div/lst-primary-display/lst-primary-display-grid/lst-primary-display-grid-shim/lst-bundle_act_core-related-list-desktop_datatable/div[2]/div/div/table/tbody/tr/th/lightning-primitive-cell-factory/span/div/lightning-primitive-custom-cell/lst-output-lookup/force-lookup/div/records-hoverable-link/div/a')
# driver.execute_script("arguments[0].click(true);", approvalid)

# approvalid=driver.find_element(By.XPATH, '//*[@id="tab-1"]/slot/flexipage-component2[2]/slot/lst-related-list-container/div/div[9]/lst-related-list-single-container/laf-progressive-container/slot/lst-related-list-single-app-builder-mapper/article/lst-related-list-view-manager/lst-common-list-internal/div/div/lst-primary-display-manager/div/lst-primary-display/lst-primary-display-grid/lst-primary-display-grid-shim/lst-bundle_act_core-related-list-desktop_datatable/div[2]/div/div/table/tbody/tr/th/lightning-primitive-cell-factory/span/div/lightning-primitive-custom-cell/lst-output-lookup/force-lookup/div/records-hoverable-link/div/a')
# driver.execute_script("arguments[0].click(true);", approvalid)
# time.sleep(5)
# approvebtn=driver.find_element(By.XPATH, "//button[normalize-space()='Approve']")
# driver.execute_script("arguments[0].click(true);", approvebtn)
# time.sleep(5)
# # windowsIDs = driver.window_handles
# # parentwindowid = windowsIDs[0]
# # print(parentwindowid)
# driver.switch_to.frame(1)
# time.sleep(5)
# driver.find_element(By.XPATH, "//textarea[@id='j_id0:j_id5:j_id35:textarea-input-01']").send_keys("Manager Approved")
# time.sleep(5)
# approvewinbtn=driver.find_element(By.XPATH, "//input[@id='j_id0:j_id5:j_id35:j_id39']")
# driver.execute_script("arguments[0].click(true);", approvewinbtn)

# reject=driver.find_element(By.XPATH, "//button[normalize-space()='Reject']")
# driver.execute_script("arguments[0].click(true);", reject)

# approvebtn=driver.find_element(By.XPATH, "//button[normalize-space()='Reassign']")
# driver.execute_script("arguments[0].click(true);", approvebtn)



# windowsIDs = driver.window_handles
# parentwindowid = windowsIDs[0]
# childwindowid = windowsIDs[1]
# childwindowid1 = windowsIDs[2]
# print(parentwindowid, childwindowid)

time.sleep(15)
#
# # time.sleep(3)
# # quote_home=driver.find_element(By.XPATH, "//span[normalize-space()='CPQ Quotes']")
# # driver.execute_script("arguments[0].click();", quote_home)
# # time.sleep(5)
# #
# account_tab=driver.find_element(By.XPATH, "//span[normalize-space()='Accounts']")
# driver.execute_script("arguments[0].click();", account_tab)
#
# time.sleep(5)
# #
# account_name=driver.find_element(By.LINK_TEXT, "Miner")
# driver.execute_script("arguments[0].click();", account_name)
# time.sleep(10)
#
# # outerframe=driver.find_element(By.XPATH, "//slot[@name='sidebar']//flexipage-component2//slot//div[@class='slds-tabs_card']")
# # driver.switch_to.frame(outerframe)
# # time.sleep(3)
#
#
# #related_record=driver.find_element(By.XPATH, "//a[@id='collaborateTab__item']")
# #driver.execute_script("arguments[0].click();", related_record)
#
# # driver.execute_script("window.scrollBy(0, 1000)")
#
# rec=driver.find_element(By.XPATH, "//span[normalize-space()='LCR-025151']")
# driver.execute_script("arguments[0].click(true);", rec)
#
# # loc_record=driver.find_element(By.XPATH, "//span[@title='Location - Customer Relationships']")
# # # driver.execute_script("arguments[0].scrollIntoView(true)", loc_record)
# # driver.execute_script("arguments[0].click(true);", loc_record)
# # driver.execute_script("return window.pageYOffset;")
# #
# # time.sleep(5)
#
# time.sleep(5)
#
# location=driver.find_element(By.XPATH, "//span[normalize-space()='National Sales']")
# driver.execute_script("arguments[0].click();", location)
# time.sleep(5)
# #
# # loc_icon=driver.find_element(By.XPATH, "//a[contains(@title,'Show 7 more actions')]//lightning-primitive-icon")
# # driver.execute_script("arguments[0].click();", loc_icon)
# # time.sleep(5)
# #
# new_opp=driver.find_element(By.XPATH, "//a[@title='New Opportunity']")
# driver.execute_script("arguments[0].click();", new_opp)
# time.sleep(5)
#
# windowsIDs = driver.window_handles
#
# parentwindowid=windowsIDs[0]  # D188312C40AB8D0198A899FE2F5E00EC
# #
# # driver.switch_to.window(parentwindowid)
# #
# # time.sleep(5)
# #
# min_sales=driver.find_element(By.XPATH, "//flowruntime-lwc-body/div[1]/flowruntime-list-container[1]/div[1]/flowruntime-base-section[1]/div[1]/flowruntime-screen-field[1]/flowruntime-lwc-field[1]/div[1]/flowruntime-radio-button-input-lwc[1]/fieldset[1]/div[1]/span[1]/label[1]/span[1]")
# driver.execute_script("arguments[0].click();", min_sales)
#
# time.sleep(5)
#
# next=driver.find_element(By.XPATH, "//button[normalize-space()='Next']")
# driver.execute_script("arguments[0].click(true);", next)
#
# time.sleep(10)
# # self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click() #Send with DocuSign Page Next 1
# # time.sleep(20)
# # self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
# # time.sleep(40)
# # self.driver.find_element(By.XPATH, "//button[@class='olv-button olv-ignore-transform css-1wtdytg']").click()
# # time.sleep(30)



























# button_link = driver.find_element_by_xpath('''//*[@id="tab-23"]/slot''')
# driver.execute_script("arguments[0].click();", button_link )