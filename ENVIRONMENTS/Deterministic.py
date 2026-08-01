class ATMAgent:

    def __init__(self):
        self.balance = 5000

    def check_balance(self):
        print("Current Balance : Rs.", self.balance)


agent = ATMAgent()

while True:

    print("\n===== DETERMINISTIC ENVIRONMENT =====")
    print("1. Check Balance")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        agent.check_balance()

    elif choice == "2":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
