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
        expected = ['Ten', 'Eleven', 'Twenty', 'Twenty-two', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
                    'Eighty', 'Ninety', 'Ninety-nine']

        for i in range(0, len(seqt)):
            self.assertEqual(NumSeq.dbl_dig(seqt[i]), expected[i])

    def test_tpl_dig(self):
        """Unittest for special cases in NumSeq"""
        seqh = [100, 101, 110, 113, 125, 500, 501, 510, 513, 536, 999]
        expecth = ['One hundred', 'One hundred and one', 'One hundred and ten', 'One hundred and thirteen',
                   'One hundred and twenty-five', 'Five hundred', 'Five hundred and one', 'Five hundred and ten',
                   'Five hundred and thirteen', 'Five hundred and thirty-six', 'Nine hundred and ninety-nine']

        for i in range (0, len(seqh)):
            self.assertEqual(NumSeq.tpl_dig(seqh[i]), expecth[i])
            # Uncomment below to print
            #print(NumSeq.tpl_dig(i))

    def test_get_tpl(self):
        seqtpl = [1, 10, 11, 100, 101, 110, 122, 999, 1000, 1001, 1010, 1013, 1020, 1234, 1204, 12345, 12305,
                123456, 123406, 123056, 1234567, 1234067, 1034567]
        expectedb = [
            [1],
            [10],
            [11],
            [100],
            [101],
            [110],
            [122],
            [999],
            [0, 1],
            [1, 1],
            [10, 1],
            [13, 1],
            [20, 1],
            [234, 1],
            [204, 1],
            [345, 12],
            [305, 12],
            [456, 123],
            [406, 123],
            [56, 123],
            [567, 234, 1],
            [67, 234, 1],
            [567, 34, 1]
        ]
        for i in range (0, len(seqtpl)):
            self.assertEqual(NumSeq.get_tpl(seqtpl[i]), expectedb[i])

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

