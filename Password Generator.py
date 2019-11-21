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
