import random

print("\nWelcome to Dank memer playground")

while True:
    playing = input("\nDo you want to play? ( Yes or No ) ").lower()

    if playing == "yes":
        print("\nOkay let's play!")
        break

    elif playing == "no":
        quit()

    else:
        print("\nInvalid Input!\nPlease try again.")


balance = 0

while True:
    print("\n1. Get started")
    print("2. Show balance")
    print("3. Beg")
    print("4. Bankrob")
    print("5. Quit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        get_started = random.randint(1, 1000)
        balance += get_started
        print(f"\nYou got started with {get_started} coins!")

    elif choice == "2":
        print(f"\nYour balance is {balance}")

    elif choice == "3":
        beg = random.randint(1, 1000)
        balance += beg
        print(f"\nOh you little poor soul, here have {beg}")

    elif choice == "4":
        outcome = random.choice(['successful', 'unsuccessful'])

        if outcome == 'successful':
            bankrob = random.randint(1, 100000)
            balance += bankrob  # Add to balance, not bankrob += balance
            print(f"\nYou robbed the bank successfully and found {bank_rob}")

        else:
            print("\nYou got caught and arrested :(")

    elif choice == "5":
        print("\nThanks for playing")
        quit()

    else:
        print("\nInvalid Input!\nPlease try again.")