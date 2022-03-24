import random

print("Welcome to the password generator!")
print("How long would you like your password?(multiples of 3)")
length = input()

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "!@#$%^&*()-+_=?"
numbers = "0123456789"
string = lower + upper + symbol + numbers
password = "".join(random.sample(string, int(length)))
count = 0



print(f"your newly generated password is {password}") 
