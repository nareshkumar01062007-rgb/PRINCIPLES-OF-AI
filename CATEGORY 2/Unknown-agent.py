class RobotAgent:

    def move(self, obstacle):

        if obstacle == "Yes":
            print("Obstacle Found")
            print("Action : Turn Right")

        elif obstacle == "No":
            print("No Obstacle")
            print("Action : Move Forward")

        else:
            print("Invalid Input")


agent = RobotAgent()

while True:

    print("\n===== UNKNOWN ENVIRONMENT =====")
    print("1. Check Path")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        obstacle = input("Obstacle Detected (Yes/No): ")

        agent.move(obstacle)

    elif choice == "2":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
