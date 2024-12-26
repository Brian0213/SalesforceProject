import time

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_Home:

    # Software BaseUrl
    baseURL = ReadConfig.getApplicationURL()
    # UserNAME
    username = ReadConfig.getUseremail()
    # Password
    password = ReadConfig.getPassword()
    # Logger command
    logger = LogGen.loggen()

    def test_Home(self, setup):
        self.driver = setup
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

        # Define HomePage Driver
        self.hp = HomePage(self.driver)
        self.hp.clickMoreBtn()
        time.sleep(5)
        self.hp.clickRatesTab()
        time.sleep(5)
        self.hp.clickMoreBtn()
        time.sleep(5)
        self.hp.clickSuppPrcTab()
        time.sleep(5)


