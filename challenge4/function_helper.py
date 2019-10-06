class fibonacci_sequence():

    def recur_fibo(n):
       """Recursive function to print Fibonacci sequence"""
       if n <= 1:
           return n
        else:
            return(recur_fibo(n-1) + recur_fibo(n-2))

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

    def fibR(n):
    if n==1 or n==2:
        return 1
    return fibR(n-1)+fibR(n-2)
    print fibR(5)

class num2str:

    def convert_num2words:
