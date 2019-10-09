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
       elif n ==1:
           return n
       else:
           return FibSeq.fib_r(n-1) + FibSeq.fib_r(n-2)

class NumSeq:

    def num2txt(self):
        """function to print numbers to text"""
        if n < 0:
            raise ValueError("Must use positive integers")