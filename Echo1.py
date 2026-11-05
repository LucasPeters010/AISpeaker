print("Welcome user.")
while True:
    data = input()
    if (data == "quit" or data == "QUIT"):
        print("Goodbye.")
        break
    else:
        print(f"You said: {data}")

