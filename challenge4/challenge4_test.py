class fibonacci_sequence():
    def fibR(n):
        """Recursive function to print Fibonacci sequence"""
        if n <= 1:
            return n
        else:
            return (fibR(n - 1) + fibR(n - 2))
    nterms=9
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(fibR(i))

class num2str:
    
    def convert_num2words:

