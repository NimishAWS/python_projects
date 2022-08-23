import random 
computer_guess = random.randint(1,10)
your_guess = int(input("Enter your any number :- "))
while computer_guess!= your_guess:
    if your_guess > computer_guess :
        print("Number is high")
        your_guess = int(input("Enter your number again :- "))
    elif your_guess < computer_guess:
        print("Number is low")
        your_guess = int(input("Enter your number again"))
    else:
        break
print("You guessed it right!!!")

