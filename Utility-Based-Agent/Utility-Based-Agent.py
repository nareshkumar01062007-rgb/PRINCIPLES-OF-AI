# Smart Light using Utility Based Agent

print("=== Smart Light using Utility Based Agent ===")

light = input("Is it Dark? (yes/no): ").lower()
preference = input("Enter preference (bright/dim): ").lower()

if light == "yes":
    if preference == "bright":
        print("💡 Light ON - Bright Mode")
    elif preference == "dim":
        print("💡 Light ON - Dim Mode")
    else:
        print("❌ Invalid Preference")
else:
    print("💡 Light OFF (Enough Natural Light)")
