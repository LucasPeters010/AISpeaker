print("Welcome user.")
while True:
    data = input()

    if (data.lower().strip() == "quit"):
        print("Goodbye.")
        break
    else:
        print(f"You said: {data}")

