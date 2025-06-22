def get_response(user_input):
    user_input = user_input.lower()
    rules = {
        "hi": "Hello there!",
        "hello": "Hi! How can I help you today?",
        "how are you": "I'm just a bunch of Python code, but I'm doing great!",
        "bye": "Goodbye! Have a nice day.",
        "thanks": "You're welcome!",
    }

    for key in rules:
        if key in user_input:
            return rules[key]
    return "Sorry, I don't understand that."

def run_chatbot():
    print("🤖 Welcome to ChatPy CLI! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: See you later!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

run_chatbot()