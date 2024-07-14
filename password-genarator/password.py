import random
chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$'
length = int(input('Enter the length of the password: '))
password = ''
for i in range(length):
    password += random.choice(chars)

print(password)