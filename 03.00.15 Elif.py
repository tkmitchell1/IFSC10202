#If you have more than two options using the conditional operator, you can use if... elif...else statement.\

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
if x > 0 and y > 0:
    print("Quadrant I")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif y > 0:
    print("Quadrant II")
else:
    print("Quadrant III")