class FanAgent:

    def set_speed(self, choice):

        if choice == "1":
            print("Fan Speed : LOW")

        elif choice == "2":
            print("Fan Speed : MEDIUM")

        elif choice == "3":
            print("Fan Speed : HIGH")

        else:
            print("Invalid Choice")


agent = FanAgent()

while True:

    print("\n===== DISCRETE ENVIRONMENT =====")
    print("1. Low Speed")
    print("2. Medium Speed")
    print("3. High Speed")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "4":
        print("Program Ended")
        break

    agent.set_speed(choice)
