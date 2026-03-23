import tkinter as tk
from tkinter import scrolledtext

from chatbot import get_response, clean_text


class ChatbotGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Rule-Based Chatbot")
        self.root.geometry("500x550")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", font=("Arial", 11))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.entry = tk.Entry(input_frame, font=("Arial", 11))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
        self.entry.bind("<Return>", self.send_message)

        send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.RIGHT)

        self.add_message("Bot", "Hello! I am a rule-based chatbot. Ask me a question.")

    def add_message(self, sender: str, message: str) -> None:
        self.chat_area.configure(state="normal")
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.configure(state="disabled")
        self.chat_area.yview(tk.END)

    def send_message(self, event=None) -> None:
        user_text = self.entry.get().strip()
        if not user_text:
            return

        self.add_message("You", user_text)
        self.entry.delete(0, tk.END)

        bot_reply = get_response(user_text)
        self.add_message("Bot", bot_reply)

        if clean_text(user_text) in {"bye", "exit", "quit"}:
            self.entry.configure(state="disabled")


if __name__ == "__main__":
    app = tk.Tk()
    ChatbotGUI(app)
    app.mainloop()
