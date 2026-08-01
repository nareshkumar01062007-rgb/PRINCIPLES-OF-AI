class LightAgent:

    def __init__(self):
        self.light = "OFF"

    def show_status(self):
        print("Current Light Status :", self.light)

    def turn_on(self):
        if self.light == "OFF":
            self.light = "ON"
            print("Light Turned ON")
        else:
            print("Light is Already ON")

    def turn_off(self):
        if self.light == "ON":
            self.light = "OFF"
            print("Light Turned OFF")
        else:
            print("Light is Already OFF")


agent = LightAgent()

while True:

    print("\n===== MODEL BASED AGENT =====")
    print("1. Show Status")
    print("2. Turn ON")
    print("3. Turn OFF")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        agent.show_status()

    elif choice == "2":
        agent.turn_on()

    elif choice == "3":
        agent.turn_off()

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")