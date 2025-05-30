import random

responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm just a bot, but I'm doing fine. How can I help you?",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I don't understand that."
}

def chatbot():
    print("ChatBot: Hi! Type something to start a conversation (type 'exit' to quit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("ChatBot: Bye!")
            break
        response = responses.get(user_input, responses["default"])
        print("ChatBot:", response)

chatbot()
