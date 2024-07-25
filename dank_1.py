import random

def main():
    print("Welcome to Dank memer playground")

playing = input("Do you want to play game? ")
if playing.lower() == "yes":
    print("Okay let's play!")
else:
    quit()

balance = 0

while True:
    print("1. Get started ")
    print("2. Show balance ")
    print("3. Beg")
    print("4. Bankrob")
    print("5. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        get_started = random.randint(1, 1000)
        balance += get_started
        print("You got started with ", get_started, " coins")
    elif choice == 2:
        print("Your balance is ", balance)
    elif choice == 3:
        beg = random.randint(1, 1000)
        balance += beg
        print("Oh you little poor soul, here have", beg)

    elif choice == 4:
        outcome = random.choice(['successful', 'unsuccessful'])
        if outcome == 'successful':
            bankrob = random.randint(1, 100000)
            balance += bankrob  # Add to balance, not bankrob += balance
            print("You robbed the bank successfully and you got", bankrob)
        else:
            print("You got caught and arrested")

    elif choice == 5:
        print("Thanks for playing")
        quit()
        

main()