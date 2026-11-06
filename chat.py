import anthropic
client = anthropic.Anthropic()

history = []


#Function to handle the input and send it to claude
def ask_claude(history):

    #Send the history of the input request "the conversation" to claude, put it's output in a variable
    response = client.messages.create(model = "claude-haiku-5-5", max_tokens = 500, messages = history, system = "Answer briefly, in one or two sentences.")

    #Give back the the last response of claude
    return response.content[0].text




print("Welcome user.")
while True:


    data = input()

    if (data.lower().strip() == "quit"):
        print("Goodbye.")
        break
    elif(data.strip() == ""):

        print("Empty input")

    else:
        #Add our new input to our history list of the user
        history.append({"role": "user", "content": data})

        try:
            reply = ask_claude(history)
            
            #Add the output of claude to our history list of "assistant"
            history.append({"role": "assistant", "content": reply})

            print(f"{reply}")

        except anthropic.APIError as error:
            history.pop()
            print(f"Call failed: {error}" )



        



