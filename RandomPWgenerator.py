import random

print("Welcome to the password generator!")
print("How long would you like your password?(multiples of 3)")
length = input()
print(length)

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "!@#$%^&*()-+_=?"
password = []
count = 0

while count < int(length):
    randlow = random.choice(lower)
    count = count + 1
    randupper = random.choice(upper)
    count = count + 1
    randsymbol = random.choice(symbol)
    count = count + 1
    password.append(randlow + randupper + randsymbol)

passwordstr = "".join(password)
print(f"your newly generated password is {passwordstr}") 
