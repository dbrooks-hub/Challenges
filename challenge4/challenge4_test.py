import unittest
from .fiblib import *

class Challenge4(unittest.TestCase):

    def setUp(self):
        print('in setup method')

    def tearDown(self):
        print('in tear down method')

    def test_fibseq(self):
        """ Unittest for FibSeq.fib"""
        seqf = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        self.assertTrue(seqf == FibSeq.fib(9), FibSeq.fib(9))
        print(seqf == FibSeq.fib(9), FibSeq.fib(9))

    def test_num2text(self):
        """ Unittest for NumSeq.num2txt"""
        dig = FibSeq.fib(10)
        for i in dig:
            print(NumSeq.num2txt(i))
            #TODO finish num2txt for hundreds & thousands

if __name__ == '__main__':
    unittest.main()

