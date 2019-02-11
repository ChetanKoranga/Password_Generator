import random
from string import ascii_letters,digits

chars = ascii_letters + "@!#$%^&*(),." + digits
print("==========Password generator==========\n")

def pwd():

    for i in range(n):
        p = ""
        j=0
        for j in range(len):
            p += random.choice(chars)
        print(p)

while True:
    n = int(input("Number of passwords to generate: "))
    len = int(input("Length of the passwords: "))



    if (n == 1):
        print("Here is your password: ", pwd())
    else:
        print("Here are your passwords: ")
        pwd()

    more = input("Do you want more passwords? (Y/N)").upper()
    if more == "Y":
        continue
    else:
        break

