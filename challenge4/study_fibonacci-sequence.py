class Fib:
# Python program to display the Fibonacci sequence up to n-th term using recursive functions

    def recur_fibo(n):
        """Recursive function to print Fibonacci sequence"""
        if n <= 1:
            return n
        else:
            return(Fib.recur_fibo(n-1) + Fib.recur_fibo(n-2))

        # Change this value for a different result
        nterms = 10

        # uncomment to take input from the user
        #nterms = int(input("How many terms? "))

        # check if the number of terms is valid
        if nterms <= 0:
            print("Please enter a positive integer")
        else:
            print("Fibonacci sequence:")
        for i in range(nterms):
            print(recur_fibo(i))

## Example 1: Using looping technique
    @staticmethod
    def fib(n):
        a,b = 1,1
        for i in range(n-1):
            a,b = b,a+b
            return a
        #print fib(5)

## Example 2: Using recursion
    @staticmethod
    def fibR(n):
        if n==1 or n==2:
            return 1
        return fibR(n-1)+fibR(n-2)
        #print fibR(5)

## Example 3: Using generators
    @staticmethod
    a,b = 0,1
    def fibI():
        global a,b
        while True:
        a,b = b, a+b
        yield a
        f=fibI()
        f.next()
        f.next()
        f.next()
        f.next()
    #print f.next()

## Example 4: Using memoization
    @staticmethod
    def memoize(fn, arg):
        memo = {}
        if arg not in memo:
            memo[arg] = fn(arg)
        return memo[arg]

## fib() as written in example 1.
fibm = memoize(fib,5)
print fibm

## Example 5: Using memoization as decorator
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, arg):
        if arg not in self.memo:
            1          self.memo[arg] = self.fn(arg)
            return self.memo[arg]

@Memoize
def fib(n):
    a,b = 1,1
    for i in range(n-):
        a,b = b,a+b
    return a
    #print fib(5)


