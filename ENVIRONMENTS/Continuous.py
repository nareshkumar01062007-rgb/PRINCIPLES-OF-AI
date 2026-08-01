class SpeedAgent:

    def check_speed(self, speed):

        if speed < 40:
            print("Status : Slow Speed")

        elif speed <= 80:
            print("Status : Normal Speed")

        else:
            print("Status : Over Speed")


agent = SpeedAgent()

while True:

    print("\n CONTINUOUS ENVIRONMENT ")
    print("1. Check Speed")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        speed = float(input("Enter Car Speed: "))

        agent.check_speed(speed)

    elif choice == "2":

        print("Program Ended")
        break

    else:

        print("Invalid Choice")
