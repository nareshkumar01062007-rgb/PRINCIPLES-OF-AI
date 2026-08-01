class QuizAgent:

    def start(self):

        print("\nSTATIC ENVIRONMENT ")
        print("Question:")
        print("What is the Capital of India?")

        answer = input("Your Answer: ")

        if answer.lower() == "delhi":
            print("Correct Answer")
        else:
            print("Wrong Answer")


agent = QuizAgent()

while True:

    print("\n1. Start Quiz")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        agent.start()

    elif choice == "2":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
