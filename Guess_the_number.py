import random

def guess(number):
    # try:
        computer = random.randint(1, 100)
        print(computer)
        while computer != number:
            if computer > number:
                print("To small")  
                number = int(input("Podaj liczbę: "))
            elif computer < number:
                print("To big")
                number = int(input("Podaj liczbę: "))
            else:
                pass
            print("You win!")
    # except ValueError:
    #     print("To nie jest liczba")

user_answer = guess(int(input("Podaj liczbę: ")))