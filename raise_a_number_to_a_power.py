# Raise a number to a power
# Many ways exist in python to calculate the xn in Python. 
# In the following script, three ways are shown to calculate the xn in Python. 
# Double ‘*’ operator, pow() method, and math.pow() method are used for calculating the xn. 
# The values of x and n are initialized with numeric values. Double ‘*’ and pow() methods are used for 
# calculating the power of integer values. math.pow() can calculate the power of fractional numbers; also, that is shown in the last part of the script.


import math
# Assign values to x and n
x = 4
n = 3

# Method 1
power = x ** n
print("%d to the power %d is %d" % (x,n,power))

# Method 2
power = pow(x,n)
print("%d to the power %d is %d" % (x,n,power))

# Method 3
power = math.pow(2,6.5)
print("%d to the power %d is %5.2f" % (x,n,power))
