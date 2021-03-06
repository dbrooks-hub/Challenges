import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import signal

class Challenge2 (unittest.TestCase):

    def setUp(self):
        print('in setup method')
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_challenge2 (self):
        print('go to copart.com')
        driver = self.driver
        driver.get("https://www.copart.com/")
        self.assertIn("Copart", driver.title)
        search_field = driver.find_element_by_id("input-search")
        search_field.click()
        search_field.clear()
        search_field.send_keys("exotic")
        search_field.send_keys(Keys.ENTER)
        search_field.submit()
        ##Spinner-NOT WORKING##
        #WebDriverWait(driver, timeout=10, poll_frequency=.5) \
            #.until(expected_conditions.invisibility_of_element_located((By.ID, "serverSideDataTable_processing")))
        time.sleep(5)
        table = driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")
        html = table.get_attribute("innerHTML")
        self.assertIn("PORSCHE", html)

if __name__ == '__main__':
    unittest.main()