import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time


class Challenge2 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2 (self):
        driver = self.driver
        driver.get("https://www.copart.com/")
        driver.find_element_by_id("input-search").click()
        driver.find_element_by_id("input-search").clear()
        driver.find_element_by_id("input-search").send_keys("exotic")
        driver.find_element_by_id ("input-search").send_keys(Keys.ENTER)
        driver.find_element_by_id("search-form").submit()
        time.sleep(5)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").clear()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").send_keys("porsche")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Remove'])[1]/following::span[4]").click()
        self.assertEqual("PORSCHE", driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Remove'])[1]/following::span[4]").text)





