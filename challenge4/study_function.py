##Syntax of Function##
#def function_name(parameters):
	#"""docstring"""
	#statement(s)

def greet(name):
    """This function greets to the person passed in as parameter"""
    print("Hello," + name + ". Good morning!")
#Doc String
print(greet.__doc__)
##Return Syntax##
#return [expression_list]#
print(greet("May"))

def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""

	if num >= 0:
		return num
	else:
		return -num

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))

#Scope & Lifetime of Variable - Example#
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

##Recursive Function##
# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))