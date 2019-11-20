import random
print('This is a Password Generator')

# Variable characters
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

length = input('How many characters would you like the password to be?')
length = int(length)

password = ''
for c in range(length):
    password += random.choice(letters)

print(password)


# This will prompt the user to enter their preference on password length
#character_length = input("How long will you like the password to be?")


# The print statement will confirm the input result for testing purposes
#print("Result = ", character_length)
