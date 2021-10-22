# Floating point number is required in programming for generating fractional numbers, 
# and sometimes it requires formatting the floating-point number for programming purposes. 
# There are many ways to exist in python to format the floating-point number. 
# String formatting and string interpolation are used in the following script to format a floating-point number. format() method with format width is used in string formatting, 
# and ‘%” symbol with the format with width is used in string interpolation. 
# According to the formatting width, 5 digits are set before the decimal point, and 2 digits are set after the decimal point.




# Use of String Formatting
float1 = 563.78453
print("{:5.2f}".format(float1))

# Use of String Interpolation
float2 = 563.78453
print("%5.2f" % float2)
