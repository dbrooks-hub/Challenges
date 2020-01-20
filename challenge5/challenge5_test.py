import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import signal

class Challenge5(unittest.TestCase):

    def setUp(self):
        print('in setup method')
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_challenge5(self):
        # print('go to copart.com')
        # driver = self.driver
        # driver.get("https://www.copart.com/")
        # self.assertIn("Copart", driver.title)
        # search_field = driver.find_element_by_id("input-search")
        # search_field.click()
        # search_field.clear()
        # search_field.send_keys("porsche")
        # search_field.send_keys(Keys.ENTER)
        # search_field.submit()
        #TODO select drop down & 100 results
        # WebDriverWait(driver, timeout=10, poll_frequency=.5) \
        #     .until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[1]')))
        # list_models = driver.find_elements(By.XPATH, '//*[@data-uname="lotsearchLotmodel"]')
        # print(len(list_models))
        # modeltext = []
        # for e in list_models:
        #     modeltext.append(e.text)
        # modeltext.sort()
        # print(modeltext)
        modeltext2 = ['', '911 CARRER', '911 CARRER', '911 GT3 RS', '911 TARGA', '944', 'BOXSTER', 'CAYENNE', 'CAYENNE', 'CAYENNE', 'CAYENNE', 'CAYENNE S', 'CAYENNE S', 'CAYENNE S', 'CAYENNE TU', 'CAYMAN S', 'CAYMAN S', 'MACAN', 'MACAN', 'MACAN S', 'PANAMERA T']
        for i in modeltext2:

        #time.sleep(5)

if __name__ == '__main__':
    unittest.main()
