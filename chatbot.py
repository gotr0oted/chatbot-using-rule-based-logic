import re
from datetime import datetime

# Dictionary-based FAQ rules (keyword -> response)
FAQ_RULES = {
    "hours": "We are open Monday to Friday, 9:00 AM to 6:00 PM.",
    "location": "Our office is in Mumbai, India.",
    "contact": "You can contact us at support@example.com.",
    "pricing": "Our basic plan starts at $9.99 per month.",
    "refund": "Yes, we offer a 7-day refund policy on all plans.",
    "help": "I can answer FAQs like hours, location, contact, pricing, and refund.",
}


def clean_text(text: str) -> str:
    """Normalize user input for easier matching."""
    return re.sub(r"\s+", " ", text.strip().lower())


def get_response(user_text: str) -> str:
    """Return chatbot response using simple rule-based logic."""
    message = clean_text(user_text)

    if not message:
        return "Please type something so I can help you."

    # if-else greeting rules
    if any(word in message for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"

    if "good morning" in message:
        return "Good morning! Hope you have a great day."

    if "good evening" in message:
        return "Good evening! How can I assist you?"

    if "time" in message:
        return f"Current time is {datetime.now().strftime('%I:%M %p')}."

    if any(word in message for word in ["bye", "exit", "quit"]):
        return "Goodbye! Have a nice day."

    # Dictionary-based FAQ lookup
    for keyword, answer in FAQ_RULES.items():
        if keyword in message:
            return answer

    return "Sorry, I don't understand that yet. Try asking about hours, location, contact, pricing, or refund."


def chat() -> None:
    print("Rule-Based Chatbot")
    print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        bot_reply = get_response(user_input)
        print(f"Bot: {bot_reply}")

        if clean_text(user_input) in {"bye", "exit", "quit"}:
            break


if __name__ == "__main__":
    chat()
