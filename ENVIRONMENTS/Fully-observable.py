class AttendanceAgent:

    def __init__(self):
        self.students = {
            "Arun": "Present",
            "Bala": "Absent",
            "Charan": "Present",
            "Deepak": "Present"
        }

    def display(self):
        print("\n===== Attendance List =====")
        for name, status in self.students.items():
            print(name, ":", status)

    def summary(self):
        present = 0
        absent = 0

        for status in self.students.values():
            if status == "Present":
                present += 1
            else:
                absent += 1

        print("\nAttendance Summary")
        print("Present Students :", present)
        print("Absent Students  :", absent)


agent = AttendanceAgent()

while True:
    print("\n===== FULLY OBSERVABLE AGENT =====")
    print("1. View Attendance")
    print("2. Attendance Summary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        agent.display()

    elif choice == "2":
        agent.summary()

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
