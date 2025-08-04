# 🎓 EduBot – College CLI Chatbot

EduBot is a simple command-line chatbot built using **Google Generative AI (Gemini API)** to help students with college-related queries like academics, events, contacts, deadlines, and more.

> 🧠 "You are EduBot, a chatbot to assist students with their college work, in any means possible."

---

## 📦 Features

- Built with Python
- Uses Google Gemini Pro model via Generative AI API
- Clean CLI interface
- Dynamically prompts for API key at startup
- Maintains short conversation history during session
- No markdown or fancy formatting — just readable plain text
- Exit with `quit`

---

## 🚀 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/edubot-cli.git
cd edubot-cli
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Python 3.8+ is recommended

### 3. Run EduBot

```bash
python main.py
```

You’ll be prompted to enter your **Google GenAI API Key** at runtime.

---

## 🔑 Where do I get an API Key?

1. Go to: [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API key"
4. Paste it when EduBot asks

---

## 🗃️ File Structure

```
edubot-cli/
├── main.py         # CLI input/output
├── chatbot.py      # Gemini API logic
├── requirements.txt
├── README.md
```

---

## 🧠 How It Works

- You enter a prompt in the CLI
- EduBot sends your prompt + system context + chat history to Gemini
- Gemini responds in plain English
- You continue the chat or type `quit` to exit

---

## 🔮 Future Plans

- Persistent chat history (session saving)
- Department-specific intents (CS, Mech, etc.)
- Telegram or web-based frontend
- Integration with syllabus PDFs or calendars

---

## 🤝 Contributing

Pull requests, issues, and suggestions are welcome. Make it better, funnier, or smarter.

---

## 📄 License

MIT License – do whatever the hell you want, just don’t be evil.

---

## 💬 Sample Usage

```
Enter your Google GenAI API Key: sk-...

🎓 EduBot is ready! Type 'quit' to exit.

You: When is the exam form submission deadline?
EduBot: The deadline is usually announced via the official portal. Please check your department notice board or portal for the exact date.

You: How do I exit this chatbot?
EduBot: Type 'quit' to exit. See you later!
```

---
