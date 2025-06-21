import random

print("Hi! How can I help you?")

data = "1234567890!@#$%^&*()_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz"

pass_len = int(input("Enter your password length: "))
quantity = int(input("Enter the number of variants you need: "))

print(f"\nYour {quantity} passwords are:")

for _ in range(quantity):
    key = ""
    for _ in range(pass_len):
        key += random.choice(data)
    print(key)
