def traffic_signal(vehicle_count):
    print("\n----- SMART TRAFFIC SIGNAL -----")

    print(f"Vehicles Detected : {vehicle_count}")

    if vehicle_count > 20:
        green_time = 60
        level = "Heavy Traffic"
    elif vehicle_count >= 10:
        green_time = 40
        level = "Moderate Traffic"
    else:
        green_time = 20
        level = "Low Traffic"

    print("Traffic Level    :", level)
    print("Green Signal Time:", green_time, "seconds")
    print("Action           : GREEN Signal ON")


while True:
    print("\n===== SIMPLE REFLEX AGENT =====")
    print("1. Check Traffic")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        vehicles = int(input("Enter number of vehicles: "))
        traffic_signal(vehicles)

    elif choice == "2":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice! Try Again.")