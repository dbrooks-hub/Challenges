import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Challenge3(unittest.TestCase):

    def setUp(self):
        print('in setup method')
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

        #### for loop ####
    def test_challenge3 (self):
        print('go to copart.com')
        driver = self.driver
        driver.get("https://www.copart.com/")
        time.sleep(5)
        self.assertIn("Copart", driver.title)
        popular_searches = driver.find_elements(By.XPATH,'//*[@ng-if=\"popularSearches\"]//a')
        WebDriverWait(driver, timeout=10, poll_frequency=.5) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@ng-if=\"popularSearches\"]//a')))
        print (len(popular_searches))
        for x in popular_searches:
            print(x.text + "-" + x.get_attribute("href"))
        self.assertIsNotNone(x.text, x.get_attribute ('href'))

        self.while_loop()
        #### while loop ####
    def while_loop (self):
        driver = self.driver
        time.sleep(5)
        popular_categories = driver.find_elements(By.XPATH, '//*[@ng-if=\"popularSearches\"]/../div[3]//a')
        WebDriverWait(driver, timeout=10, poll_frequency=.5) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@ng-if=\"popularSearches\"]/../div[3]//a')))
        i = 0
        while i < len(popular_categories):
            print(popular_categories[i].text + "-" + popular_categories[i].get_attribute ("href"))
            i += 1
        #self.assertIsNotNone(popular_categories[i].text, popular_categories[i].get_attribute ("href"))
        #i += 1 (NOT WORKING...do I need this?)

if __name__ == '__main__':
    unittest.main()