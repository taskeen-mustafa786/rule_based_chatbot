responses = {
    "hi":"Hello! 👋 How can I assist you today?",
    "how are you?":"I'm doing great! Thanks for asking. How can I help you?",
    "bye":"Goodbye! 👋 Have a great day.",
    "thanks":"You are welcome!",
    "exit":"Chat ended. See you next time!",
}

def chatbot(responses=responses):
    print("Chatbot: Hello! I am a rule-based chatbot. Type 'exit' to end the chat.")
    is_there_more = True

    while is_there_more:
        user = input("You: ").lower()
    
        response = responses.get(
        user,
        "I don't understand"
        )
        print("Chatbot: ",response)
        if user == "exit":
            is_there_more = False

chatbot()

