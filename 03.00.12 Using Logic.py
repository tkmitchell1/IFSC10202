#If you need to check that two numbers n and m are both even, you should check both n % 2 == 0 and m % 2 == 0

n = int(input("Enter first value: "))
m = int(input("Enter second value: "))
 
if n % 2 == 0 and m % 2 == 0:
    print("Both Numbers are Even")
else:
    print("One of the Numbers is not Even")