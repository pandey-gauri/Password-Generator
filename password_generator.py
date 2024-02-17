import random

print("Welcome to the Password Generator!")

display = int(input("Enter the amount of random passwords to generate: "))
length = int(input("Enter the length of the password: "))
print("\nHere are the passwords")
char = 'abcdefghijklmnopqrstuvwxyz@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(display):
  pwd = ""
  for c in range(length):
    pwd += random.choice(char)
  print(pwd)
print("Thankyou for using the Password Generator!")
