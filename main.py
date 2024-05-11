from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = Bot(token='7188890855:AAGOR_3iZSjZqk3DSFiMfZrA1bRbvKsngYs')

def send_message_to_user(update: Update, context: CallbackContext) -> None:
    # Get the message text
    message_text = update.message.text

    # Extract the username from the message
    username = message_text.split('@')[1].strip()

    # Get the user ID based on the username
    user_id = context.bot.get_chat(username).id

    # Text to send
    message_to_send = 'test one'

    # Send the message to the user
    context.bot.send_message(chat_id=user_id, text=message_to_send)

def main() -> None:
    updater = Updater('7188890855:AAGOR_3iZSjZqk3DSFiMfZrA1bRbvKsngYs')
    dispatcher = updater.dispatcher

    # Message handler to send messages to users
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex(r'^/user @\w+'), send_message_to_user))

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
