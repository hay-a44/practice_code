from random import randint
password=""
for i in range(8):
    i= chr(randint(65,90))
    password= str(password) + i
#65-98 are the letter in upper case in randint
for j in range(2):
    j= (randint(0,9))
    j=str(j)
    password=str(password) + j

print(password)
