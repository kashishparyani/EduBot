from Chatbot import setup_model, get_bot_response

def main():
    api_key = input("Enter your Google GenAI API Key: ").strip()
    model = setup_model(api_key)

    if not model:
        print("Invalid API key or setup failed.")
        return

    context = "Helping students with college academics, event details, submissions, contacts, and general guidance."
    history = []

    print("\n🎓 EduBot is ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("EduBot: Bye!")
            break

        history_text = "\n".join(history[-5:])  # limit history size to last 5
        response = get_bot_response(model, user_input, history_text, context)
        print(f"EduBot: {response}\n")

        history.append(f"You: {user_input}")
        history.append(f"EduBot: {response}")

if __name__ == "__main__":
    main()
