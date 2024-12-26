import time

import pytest
from Pages.LoginPage import LoginPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*****Starting The Login Test*****")
        # Call the Browser Configuration
        self.logger.info("*****Call the Browser Configuration*****")
        self.driver = setup
        # Ten seconds wait before launch
        self.driver.implicitly_wait(10)
        # Open the Website URL
        self.logger.info("*****Open the Website URL*****")
        self.driver.get(self.baseURL)
        # Fit the browser screen
        self.logger.info("*****Fit the browser screen*****")
        self.driver.maximize_window()
        # Define LoginPage Driver
        self.logger.info("*****Define LoginPage Driver*****")
        self.lp = LoginPage(self.driver)
        # Fill the UserName field
        self.logger.info("*****Fill the UserName field*****")
        self.lp.setUserName(self.username)
        # Fill the Password field
        self.logger.info("*****Fill the Password field*****")
        self.lp.setPassword(self.password)
        # Click on the Signin Button
        self.logger.info("*****Click the Signin Button*****")
        self.lp.clickSignin()
        time.sleep(5)
        # Click on the SetUp Icon
        self.logger.info("****** Click on the Setup Icon ******")
        self.lp.clickSetUp()
        # Click on the Logout Button
        self.logger.info("****** Click on the Logout button******")
        self.lp.clickLogOut()
        time.sleep(5)
        # Executing Assertions
        act_title = self.driver.title
        print(act_title)
        if act_title == "Login | Salesforce":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
        self.logger.info("*****Login Test Completed*****")
        # Close the Browser Window
        self.driver.quit()




