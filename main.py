inv = []
inv = str(inv)
Money = 0
m = str(Money)
run = True
print("Welcome To Farming Simulator!")
print("To Farm Just Type f!")
print("And That Way You Will Gain Money!")
print("To View Your Money,Just Type m")
print("Lets Start!")
while run:
Input = input()
if Input == "f!":
print("You Farmed And Gained 40 Dollars!")
Money = Money+40
print(Money)
print("Thats Your Current Balance")
if Input == "m":
print("Balance Is:"+ Money)
