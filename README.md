# Telegram Bot Message Viewer

This example shows how to receive messages from a Telegram bot and display them on a simple web page using Flask.

## Requirements

- Python 3.8+
- `python-telegram-bot` library
- `Flask`

Install dependencies:

```bash
pip install python-telegram-bot==20.* Flask
```

## Usage

1. Create a Telegram bot with [BotFather](https://t.me/BotFather) and obtain the bot token.
2. Set the environment variable `TELEGRAM_BOT_TOKEN` to your bot token.
3. Run the application:

```bash
python app.py
```

Open `http://localhost:5000` in your browser to see incoming messages.

Messages sent to your bot will appear in the list.
