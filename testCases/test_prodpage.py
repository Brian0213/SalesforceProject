import time

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.ProductsPage import ProductsPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen

class Test_ProductsPage:

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
        time.sleep(3)

        # Define HomePage Driver
        self.hp = HomePage(self.driver)
        self.hp.clickProductsTab()
        time.sleep(3)

        # Define ProductsPage Driver
        self.logger.info("*****Starting The Product Page Test*****")
        self.pp = ProductsPage(self.driver)
        # Clicking on the Products Nav Button.
        self.pp.clickProductsBtn()
        time.sleep(3)
        # Clicking on the Products Missing Line or Activity Type Tab
        # self.pp.clickProdMissTab()
        # time.sleep(3)
        # # Clicking on the Products Nav Button.
        # self.pp.clickProductsBtn()
        # time.sleep(3)
        # # Clicking on the All Products Tab.
        # self.pp.clickAllProductsTab()
        # time.sleep(3)
        # # Clicking on the Products Nav Button.
        # self.pp.clickProductsBtn()
        # time.sleep(3)
        # # Clicking on the Integrated Products Tab.
        # self.pp.clickIntegratedProdTab()
        # time.sleep(3)
        # Clicking on the Products Nav Button.
        # self.pp.clickProductsBtn()
        # time.sleep(3)
        # Clicking on the Stockable Products Tab.
        self.pp.StockableProductsTab()
        time.sleep(3)
        # Clicking on the Products Nav Button.
        self.pp.clickProductsBtn()
        time.sleep(3)
        # Clicking on the Recently Viewed Tab.
        self.pp.RecentlyViewedTab()
        time.sleep(3)
        self.logger.info("*****Product Page Test Completed*****")
        self.driver.quit()




