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
        #Uncomment below to print
        #print(seqf == FibSeq.fib(9), FibSeq.fib(9))

    def test_dbl_dig(self):
        """Unittest for the function dbl_dig"""
        seqt = [10, 11, 20, 22, 30, 40, 50, 60, 70, 80, 90, 99,]
        expected = [Ten, Eleven, Twenty, Twenty-two, Thirty, Forty, Fifty, Sixty, Seventy, Eighty, Ninety, Ninety-nine]
        for i in seqt:
            print(NumSeq.dbl_dig(i))
            #Todo add unittest for dbldig & add assertions

    def test_tpl_dig(self):
        # TODO change to unittest for tpldig & add assertions
        """Unittest for special cases in NumSeq"""
        seqh = [100, 101, 110, 113, 125, 500, 501, 510, 513, 536, 999]
        for i in seqh:
            print(NumSeq.tpl_dig(i))

    def test_get_tpl(self):
        seqtpl = [1, 10, 11, 20, 22, 99, 100, 101, 109, 110, 111,
                120, 122, 999, 1000, 1001, 1010, 1013, 1020, 1022, 1234, 1204, 1034, 12345, 12305,
                12045, 10345, 123456, 123406, 123056, 120456, 103456, 1234567, 1234507, 1234067, 1230567, 1204567, 1034567]

        sget = NumSeq.get_tpl(seqtpl)
        stxt = NumSeq.num2txt(seqtpl)
        assert len(sget) == len(seqtpl)
        assert len(stxt) == len(seqtpl)
        assert len(sget) == len(stxt)

        for i in range (0, len(seqtpl)):
            print(i)

            #TODO add unittest for get tpl & add assertions


    def test_num2text(self):
        """ Unittest for NumSeq.num2txt"""
        dig = FibSeq.fib(30)
        for i in dig:
            # TODO assertions
            print(NumSeq.num2txt(i))

    def test_get_fib_seq_with_text(self):

        print(FibSeqFactory)
        #TODO add FibFactory test & assertions

if __name__ == '__main__':
    unittest.main()

