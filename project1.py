def simple_chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot. (Type 'bye' to exit)")
    
    while True:
        # Get input from the user and convert to lowercase for easy matching
        user_input = input("You: ").lower().strip()
        
        # 1. Check for exit command
        if user_input == "bye" or user_input == "exit":
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
            
        # 2. Check for greetings
        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("Chatbot: Hello there! How can I help you today?")
            
        # 3. Check for identity/name questions
        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot: I am a basic Python chatbot built using if-else logic!")
            
        # 4. Check for small talk / well-being
        elif "how are you" in user_input or "how's it going" in user_input:
            print("Chatbot: I am doing great, thank you! I don't sleep, so I never feel tired.")
            
        # 5. Check for help or capabilities
        elif "help" in user_input or "what can you do" in user_input:
            print("Chatbot: I can greet you, tell you my name, or say goodbye. Try asking 'who are you'!")
            
        # 6. Fallback if no keywords match
        else:
            print("Chatbot: I'm sorry, I don't understand that keyword yet. Could you try rephrasing?")

# Run the chatbot program
if __name__ == "__main__":
    simple_chatbot()
