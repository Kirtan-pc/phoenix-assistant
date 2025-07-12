# Phoenix Assistant 🔥

Phoenix is a voice-activated virtual assistant built in Python. It uses speech recognition, text-to-speech, and generative AI to perform tasks like opening websites, playing music, fetching news, and answering questions.

---

## Features

- Voice-activated control
- Opens popular websites (Google, YouTube, Facebook)
- Plays music from a custom library
- Fetches top news headlines via NewsAPI
- Answers questions using Gemini AI (Google's generative model)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/phoenix-assistant.git
cd phoenix-assistant
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

---

## API Keys

You need:

- NewsAPI.org key – for news headlines
- Gemini AI (Google) key – for generative answers

You can hardcode them in `main.py` (as in the example) or store them in a `.env` file (recommended).

---

## Usage

Run the assistant with:

```bash
python main.py
```

Say **"Phoenix"** to activate it, then speak a command like:

- “Open Google”
- “Play [song name]”
- “Give me the news”
- “What is the capital of France?”

Say **"stop"**, **"sleep"**, or **"bye"** to shut it down.

---

## Project Structure

```
phoenix-assistant/
│
├── main.py             # Main assistant script
├── musicLibrary.py     # Dictionary of songs and links
├── requirements.txt    # Python package list
├── .gitignore          # Files/folders Git should ignore
├── README.md           # This file
└── venv/                # Virtual environment (ignored by Git)
```

---

## .gitignore

```
venv/
__pycache__/
*.pyc
.env
```

---

## Notes

- Ensure your microphone works and system permissions allow recording.
- For better API key management, consider using a `.env` file with `python-dotenv`.

---

## License

MIT License
