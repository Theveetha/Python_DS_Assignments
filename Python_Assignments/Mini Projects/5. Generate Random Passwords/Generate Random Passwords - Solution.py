
# __________________Tasks_________________

'''
Create a program to generate passwords for you.

You have to create a Program that asks user total passwords he needed and the length of them.

Sample Shown in Folder

'''

import random
import string

'''
print(string.punctuation)
print(string.ascii_letters)
print(string.digits)
'''


characters = string.ascii_letters + string.digits + string.punctuation

totalPass = int(input("How many passwords : "))
pass_len = int(input("Password Length : "))

for i in range(totalPass) :
    password = random.sample(characters, pass_len)
    password = "".join(password)
    print(password)
















