import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Using_Essential_Oils(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        print('Opening Browser')

    def tearDown(self):
        self.driver.close()
        print('In teardown')

    def test_using_essential_oils(self):
        driver = self.driver
        driver.get("https://www.doterra.com/US/en/using-essential-oils")
        self.assertIn("How to Use Essential Oils", driver.title)
        #most_popular = driver.find_elements(By.XPATH, '//*[@id=\"content_body\"]//ol[1]/li')
        #WebDriverWait(driver, timeout=10, poll_frequency=.5) \
            #.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id=\"content_body\"]//ol[1]/li')))
        #print(len(most_popular))
        #for x in most_popular:
            #print(x.text + "-" + x.get_attribute("href"))

        #self.while_loop()
# method?
    #def while_loop(self):
        #driver = self.driver
        time.sleep(5)
        most_popular = driver.find_elements(By.XPATH, '//*[@id=\"content_body\"]//ol[1]/li')
        WebDriverWait(driver, timeout=10, poll_frequency=.5) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id=\"content_body\"]//ol[1]/li')))
        i = 0
        while i < len(most_popular):
            print(most_popular[i].text + "-" + most_popular[i].get_attribute("href"))
            i += 0
        # Assertions

if __name__ == '__main__':
    unittest.main()