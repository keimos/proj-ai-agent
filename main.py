# Simple AI Agent

def simple_ai_agent():
    print("AI Agent: Hello! I'm you simple AI assistant. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input in ["quit, "exit", "bye"]:
            print("AI Agent: Goodbye!")
            break