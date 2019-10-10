import unittest
from .fiblib import *


class Challenge4(unittest.TestCase):

    def setUp(self):
        print('in setup method')

    def tearDown(self):
        print('in tear down method')

    def test_fibseq(self):
        seqf = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        self.assertTrue(seqf == FibSeq.fib(9), FibSeq.fib(9))
        print(seqf == FibSeq.fib(9), FibSeq.fib(9))

    def test_fibseq_r(self):
        nval = 9
        for i in range (nval):
            print(FibSeq.fib_r(i))

    #def test_num2text(self):
        #singledig = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        #teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        #tens = ["ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        #secondval = 5
        #leastsignval = 1
        #print(singledig[leastsignval]) = > one
        #print(tens[secondval]) = > fifty
        #concantionate strings
        # print(tens[secondval] + singledig[leastsignval]) = > fiftyone



if __name__ == '__main__':
    unittest.main()

