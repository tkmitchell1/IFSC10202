from random import randint
print("Winners and Losers - Human is Even, Computer is Odd")
humanscore = 0
computerscore = 0
for i in range(1, 6):
    print("Round", i)
    human = input("Enter a number 1-5:")
    print("human is: " + human)
    computer = randint(1,5)
    print("computer is: " + str(computer))
    value = (int(human) + computer)
    if (value % 2) == 0:
        print(f"{value} is even")
        humanscore += 1
        print("human score: " + str(human))
    else:
        print(f"{value} is odd")
        computerscore += 1
        print("computer score: " + str(computer))
print(f"Human score: " + str(humanscore))
print(f"Computer score: " + str(computerscore))
print(humanscore)
print(computerscore)
if humanscore > computerscore:
    print("Human wins")
else:
    print("Computer wins")

