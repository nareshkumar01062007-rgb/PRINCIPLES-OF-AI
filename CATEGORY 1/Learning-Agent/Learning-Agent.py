# Smart Light using Learning Agent

print("=== Smart Light using Learning Agent ===")

light = input("Is it Dark? (yes/no): ").lower()

if light == "yes":
    print("💡 Light ON")
    print("Learning: Next time, when it is dark, turn ON the light.")
else:
    print("💡 Light OFF")
    print("Learning: Next time, when there is enough light, keep the light OFF.")
