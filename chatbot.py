
print("Bot: Hello! I am a basic chatbot.")
print("Bot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I'm doing great! How are you?")

    elif "your name" in user:
        print("Bot: My name is Python Bot.")

    elif "what can you do" in user:
        print("Bot: I can answer some basic questions.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
