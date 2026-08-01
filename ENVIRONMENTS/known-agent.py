class CalculatorAgent:

    def calculate(self, a, b, choice):

        if choice == 1:
            print("Result =", a + b)

        elif choice == 2:
            print("Result =", a - b)

        elif choice == 3:
            print("Result =", a * b)

        elif choice == 4:
            if b != 0:
                print("Result =", a / b)
            else:
                print("Division by Zero is not possible")

        else:
            print("Invalid Choice")


agent = CalculatorAgent()

while True:

    print("\n===== KNOWN ENVIRONMENT =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program Ended")
        break

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    agent.calculate(a, b, choice)
