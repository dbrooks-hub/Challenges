#####Operatiors and Functions#####
#fibonacci sequence#
def fibr(n):
    if n==1 or n==2:
        return 1
    return fibr(n-1)+fibr(n-2)
    print fibr(5)

import unittest
from selenium import webdriver

class Challenge4(unittest.TestCase):



    def setUp(self):
        print('in setup method')
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_challenge4(self):
        #print()
        driver = self.driver
        driver.get("https://www.copart.com")
        self.assertIn("Copart", driver.title)


if __name__ == '__main__':
    unittest.main()