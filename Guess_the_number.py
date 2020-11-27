import random

def get():
    """Get number from user"""
    while True:
        try:
            user = int(input("Guess the number: "))
            break
        except ValueError:
            print("To nie jest liczba")
    return user

def guess():
    """Check if user number is equal to computer random generated"""
    user_answer = get()
    computer = random.randint(1, 100)
    while user_answer != computer:
        if computer > user_answer:
            print("To small")
        else:
            print("To big")
        user_answer = get()
    print("You win")

guess()
