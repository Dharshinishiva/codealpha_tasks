def chatbot():
    print("Chatbot: Hello! Type something to talk (type 'bye' to exit)")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi!")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: I don't understand.")


chatbot()
