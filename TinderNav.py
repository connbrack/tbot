import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TinderNav:
    def __init__(self, driver=None):
        """
        Initializes an instance of TinderNav.
        """
        self.driver = driver

    def createDriver(self):
        """
        Creates and returns a new Chrome webdriver with specified options.
        """
        file_dir = os.path.dirname(__file__)
        data_dir = os.path.join(file_dir, 'browser-data')

        options = uc.ChromeOptions()
        options.headless = False
        options.add_argument("--enable-geolocation")
        options.add_argument(f"--user-data-dir={data_dir}")
        driver = uc.Chrome(options=options)
        self.driver = driver

    def login(self):
        """
        Manages the login process. If already logged in, notifies the user. 
        Otherwise, prompts user to manually log in.
        """
        time.sleep(3)
        if self.driver.current_url == 'https://tinder.com/app/recs':
            print('looks like you are already logged in!')
        else:
            input("Please manually login, press enter when login is complete..")

    def load_webpage(self):
        """
        Loads the main Tinder app webpage.
        """
        url = "https://tinder.com/app/"
        self.driver.get(url)

    def wait_for_like_button(self, wait_for_reload_time=60):
        WebDriverWait(self.driver, wait_for_reload_time).until(EC.element_to_be_clickable((By.XPATH, "//button[span/span/span[text()='Like']]")))

    def like(self):
        """
        Finds and clicks the 'Like' button on Tinder.
        """
        button = self.driver.find_element(
            By.XPATH, "//button[span/span/span[text()='Like']]")
        button.click()

    def dislike(self):
        """
        Finds and clicks the 'Nope' button on Tinder.
        """
        button = self.driver.find_element(
            By.XPATH, "//button[span/span/span[text()='Nope']]")
        button.click()

    def quit(self):
        """
        Closes the webdriver and quits the browser.
        """
        self.driver.quit()
