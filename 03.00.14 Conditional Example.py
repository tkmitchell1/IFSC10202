#Let's check that the number a is positive and the number b is non-negative:
#if a > 0 and not (b < 0):
#Instead of not (b < 0) we can write (b >= 0)

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
if a > 0 and b >= 0:
# another suitable expression is
# if a > 0 and not (b < 0):
    print('A is greater than 0 and B is greater than or equal to 0')
else:
    print('Either A is less then or equal to zero or B is less than 0')