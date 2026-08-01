# Smart Light using Goal Based Agent

print("=== Smart Light using Goal Based Agent ===")

light = input("Is it Dark? (yes/no): ").lower()
goal = input("Goal (study/sleep): ").lower()

if goal == "study":
    if light == "yes":
        print("💡 Light ON")
    else:
        print("💡 Light is already ON")
elif goal == "sleep":
    print("💡 Light OFF")
else:
    print("Invalid Goal")
