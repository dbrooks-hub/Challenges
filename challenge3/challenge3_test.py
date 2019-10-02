import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge3 (self):
        driver = self.driver
        driver.get("https://www.copart.com/")
        time.sleep(5)
        popular_searches = driver.find_elements(By.XPATH,'//*[@ng-if="popularSearches"]//a')
        WebDriverWait(driver, timeout=10, poll_frequency=.5) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@ng-if="popularSearches"]//a')))
        print (len(popular_searches))
        for x in popular_searches:
            print(x.text + "-" + x.get_attribute("href"))

        #Finish with while Loop & add assertions
        #popular_categories = self.driver.find_elements('//*[@ng-if="popularSearches"]//a')
        #print(len(popular_categories))
        #while x in popular_categories:
            #print(x.text + "-" + x.get_attribute("href"))


        #self.assertIn('')



