def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")
        elif user_input in ["how are you?", "how are you doing?"]:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        elif user_input in ["what is your name?", "who are you?"]:
            print("Chatbot: I'm a simple rule-based chatbot.")
        elif user_input in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that.")
            

if __name__ == "__main__":
    chatbot()