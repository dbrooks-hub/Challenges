import unittest
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge4(self):
        driver = self.driver
        driver.get("https://www.copart.com")
        self.assertIn("Copart", driver.title)


if __name__ == '__main__':
    unittest.main()