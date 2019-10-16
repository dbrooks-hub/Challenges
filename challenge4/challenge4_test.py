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

    #def fibseq_r_test(self):
        #nval = 9
        #for i in range (nval):
            #print(FibSeq.fib_r(i))

    def test_num2text(self):
        dig = FibSeq.fib(9)
        for i in dig:
            print(NumSeq.num2txt(i))



if __name__ == '__main__':
    unittest.main()

