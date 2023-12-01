import string
import random
n=int(input("Enter your password lenght: "))
print(''' Choose your combinations of password
           1. digits
           2. letters
           3.special characters
           4.exit!''')
characterlist=""
while(True):
    choice=int(input("pick a choice "))
    if(choice == 1):
        characterlist += string.ascii_letters
    elif(choice == 2):
        characterlist += string.digits
    elif(choice == 3):
        characterlist += string.punctuations
    elif(choice == 4):
        break
    else:
        print("Please pick a valid choice")
password = []
for i in range(n):
    randomchar=random.choice(characterlist)
    password.append(randomchar)
print("The random password is: "+"".join(password))
