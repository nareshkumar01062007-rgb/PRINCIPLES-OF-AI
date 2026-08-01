class DrivingAgent:

    def check(self, visibility, obstacle):

        print("\n===== Driving Decision =====")

        if visibility == "Poor" and obstacle == "Yes":
            print("Action : Stop Vehicle")

        elif visibility == "Poor":
            print("Action : Drive Slowly")

        elif obstacle == "Yes":
            print("Action : Apply Brake")

        else:
            print("Action : Drive Normally")


agent = DrivingAgent()

while True:

    print("\n===== PARTIALLY OBSERVABLE AGENT =====")
    print("1. Check Driving")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        visibility = input("Visibility (Good/Poor): ")
        obstacle = input("Obstacle (Yes/No): ")

        agent.check(visibility, obstacle)

    elif choice == "2":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
