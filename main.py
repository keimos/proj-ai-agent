# Simple AI Agent

def simple_ai_agent():
    print("AI Agent: Hello! I'm you simple AI assistant. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input in ["quit", "exit", "bye"]:
            print("AI Agent: Goodbye!")
            break
        elif "hello" in user_input:
            print("AI Agent: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("AI Agent: I'm just a program, but thanks for asking! How can I help you?")
        elif "your name" in user_input:
            print("AI Agent: I'm a simple AI agent without a name. You can call me AI!")
        else:
            print("AI Agent: I'm not sure how to respond to that. Can you ask something else?")
        print("AI Agent: I'm here to help you with simple questions and tasks.")

# Run the AI agent
if __name__ == "__main__":
    simple_ai_agent()