class FibSeqFactory:
    def __init__(self, number=0):
        self.number = number

    def get_fib_seq_with_text(self):
        """
        This method calls FibSeq.fib and gets the fib seq in an array, like this:
            [0,1,1,2,3,5,8]

            We then pass that to NumSeq.num2txt and get a result like:
            ['zero', 'one','one','two', 'three', 'five', 'eight']

            The final operation is to return an array that contains both of
            these arrays joined by ' - '
        """
        num_seq = FibSeq.fib(self.number)
        text_seq = NumSeq.num2txt(num_seq)

        assert len(num_seq) == len(text_seq)

        to_return = []
        for i in range(0, len(num_seq) - 1):
            to_return[i] = str(num_seq[i]) + ' - ' + text_seq[i]

        return to_return



class FibSeq:

    def fib(n):
        to_return = []
        for i in range(0,n):
            to_return.append(FibSeq.fib_r(i))

        return to_return

    def fib_r(n):
       """Recursive function to print Fibonacci sequence"""
       if n < 0:
           raise ValueError("Must use positive integers")
       if n == 0:
           return n
       elif n == 1:
           return n
       else:
           return FibSeq.fib_r(n-1) + FibSeq.fib_r(n-2)

class NumSeq:

    @staticmethod
    def num2txt(num):
        """function to print numbers to text"""
        numdict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                     10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", \
                     17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", \
                   60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        bigs = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintrillion', 'sextillion', 'septillion']

        if num < 0:
            raise ValueError("Must use positive integers")

        #THIS IS NOT WORKING
        if(1 <= num < 19):
            return(numdict[num])
        elif 20 <= num < 99:
            tens, below_ten = divmod(num, 10)
            return((numdict[tens - 2] + '-' + str(numdict[below_ten].lower)))
