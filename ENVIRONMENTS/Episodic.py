class SpamAgent:

    def check_email(self, email):

        if "offer" in email.lower():
            print("Spam Email")

        else:
            print("Normal Email")


agent = SpamAgent()

while True:

    print("\n===== EPISODIC ENVIRONMENT =====")
    print("1. Check Email")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        email = input("Enter Email Subject: ")

        agent.check_email(email)

    elif choice == "2":

        print("Program Ended")
        break

    else:

        print("Invalid Choice")
