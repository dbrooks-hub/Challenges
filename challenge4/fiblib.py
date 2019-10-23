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
    @staticmethod
    def fib(n):
        """This method captures Fibonacci sequence in the specified range in an array
            example: Fibseq.fib_r(9) -> [0,1,1,2,3,5,8,13,21]"""
        to_return = []
        for i in range(0, n):
            to_return.append(FibSeq.fib_r(i))

        return to_return
    @staticmethod
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
        """This method uses dictionary and array to function to print numbers to text"""
        numdict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                     10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", \
                     17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", \
                   60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        bigs = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion']

        if num < 0:
            raise ValueError("Must use positive integers")
        if (num == 0):
            return (numdict[num])
        if(1 <= num <= 19):
            return(numdict[num])
        elif(20 <= num <= 99):
            tens, below_ten = divmod(num, 10)
            return((numdict[tens * 10] + '-' + str(numdict[below_ten].lower())))
        #WIP.
        # Thinking I need to turn the two digit and 3 digit into seperate functions to call for each 3 digit integer return?
        # Below isn't working.
        # Call the two digit for less than 20 with following special cases:
        # Address: 0 in tens for [01, 02,03,04,05,06,07,08,09,]
        # Address: adding the word "and " for the above as well as [10,11,12,13,14,15,16,17,18,19]
        # Call the two digit for greater than 20
        elif(100 <= num <= 999):
            hundreds = divmod(num, 100)
            if num >= 10:
                sngl = divmod(num, 10).lstrip ('0')
                #(sngl.lstrip('0')) ?
            return(numdict[hundreds] + ' hundred and' + str(numdict[sngl]))
            if 20 <= num <=99:
                tens, below_ten = divmod(num, 10)
            return(((numdict[hundreds] + 'hundred ' + (numdict[tens * 10] + '-' + str(numdict[below_ten].lower)))))

        #WIP - All the Bigs (pairs of 3)

        #while(num > 999)
            #num =
