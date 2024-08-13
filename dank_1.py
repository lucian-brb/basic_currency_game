
import random
from config_handler import load_data, save_data
from utils import get_started
data = load_data()

 


print("\nWelcome to Dank memer playground")

while True:
    playing = input("\nDo you want to play? ( Yes or No ) ").lower()

    if playing == "yes":
        result = get_started()  # Assign the return value to a variable
        print(f"\nYou got started with {result} coins!")
        data["balance"] = result  # Set the initial balance
        save_data(data)  # Save the changes
        break

    elif playing == "no":
        quit()

    else:
        print("\nInvalid Input!\nPlease try again.")

while True:
    
    print("1. Show balance")
    print("2. Beg")
    print("3. Bankrob")
    print("4. Quit\n")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print(f"\nYour balance is {data['balance']}")

    elif choice == "2":
        beg_amount = random.randint(1, 1000)
        data["balance"] += beg_amount
        save_data(data)  # Save the changes
        print(f"\nOh you little poor soul, here have {beg_amount}")

    elif choice == "3":
        outcome = random.choice(['successful', 'unsuccessful'])

        if outcome == 'successful':
            bankrob_amount = random.randint(1, 100000)
            data["balance"] += bankrob_amount
            save_data(data)  # Save the changes
            print(f"\nYou robbed the bank successfully and found {bankrob_amount}")

        else:
            print("\nYou got caught and arrested :(")

    elif choice == "4":
        print("\nThanks for playing")
        quit()

    else:



        print("\nInvalid Input!\nPlease try again.")