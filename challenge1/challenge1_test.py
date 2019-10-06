import unittest
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        print ('in setup method')
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_challenge1(self):
        print ('go to google')
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)

if __name__ == '__main__':
    unittest.main()
