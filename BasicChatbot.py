
def chatbot():
    print("===== SIMPLE CHATBOT =====")
    print("Hello! I am your Python Chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user = input("\nYou: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Python Chatbot.")

        elif user == "what can you do":
            print("Bot: I can chat with you!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
