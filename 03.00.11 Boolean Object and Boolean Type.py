#you can assign numbers to such variable: a = 0 or a = 1. This is because Python treats 0 as False and treats 1 as True. 

print(bool(-10))    # True
print(bool(0))      # False - zero is the only false number
print(bool(10))     # True
 
print(bool(''))     # False - empty string is the only false string
print(bool('abc'))  # True