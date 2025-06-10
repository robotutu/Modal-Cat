import os
import asyncio
from flask import Flask, render_template_string
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

messages = []

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<title>Telegram Messages</title>
<h1>Received messages</h1>
<ul>
{% for m in messages %}
<li><strong>{{m['from']}}</strong>: {{m['text']}}</li>
{% endfor %}
</ul>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, messages=messages)

async def handle_message(update: Update, context):
    user = update.effective_user.first_name if update.effective_user else 'Unknown'
    text = update.message.text if update.message else ''
    messages.append({'from': user, 'text': text})

async def run_polling(application):
    while True:
        await application.process_updates()  # fetch new updates
        await asyncio.sleep(1)

if __name__ == '__main__':
    if not TOKEN:
        raise RuntimeError('Set TELEGRAM_BOT_TOKEN env var')

    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    import threading, asyncio
    def start_polling():
        asyncio.run(run_polling(application))

    threading.Thread(target=start_polling, daemon=True).start()
    app.run(debug=True)
