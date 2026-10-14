import random

class WeatherAgent:

    def predict(self):

        weather = ["Sunny", "Rainy", "Cloudy"]

        print("Today's Weather :", random.choice(weather))


agent = WeatherAgent()

while True:

    print("\n===== STOCHASTIC ENVIRONMENT =====")
    print("1. Predict Weather")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        agent.predict()

    elif choice == "2":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
