import unittest
from .fiblib import *
from .num_text_conversion import *

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
    def test_threedig(self):
        """Unittest for special cases in NumSeq"""
        seqh = [100, 101, 109, 110, 113, 125, 196, 500, 501, 509, 510, 513, 536, 999, 1000, 1001, 1010, 1013, 1020, 1025]
        for i in seqh:
            print(NumSeq.num2txt(i))

    def test_num2text(self):
        """ Unittest for NumSeq.num2txt"""
        dig = FibSeq.fib(14)
        for i in dig:
            print(NumSeq.num2txt(i))
            #TODO finish num2txt for hundreds & thousands

if __name__ == '__main__':
    unittest.main()

