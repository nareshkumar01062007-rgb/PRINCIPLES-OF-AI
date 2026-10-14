import time

class TrafficSignalAgent:

    def start(self):

        print("\n===== DYNAMIC ENVIRONMENT =====")

        for i in range(5, 0, -1):
            print("Green Signal :", i, "seconds")
            time.sleep(1)

        print("Red Signal ON")


agent = TrafficSignalAgent()

while True:

    print("\n1. Start Signal")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        agent.start()

    elif choice == "2":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
