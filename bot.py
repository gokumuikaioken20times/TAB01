from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the start function
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot. How can I help you?")
    
    # Define the start function
def help(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot. How can I help you?")

# Define the main function
def main():
    # Replace 'YOUR_API_TOKEN' with your actual bot token
    API_TOKEN = "YOUR_API_TOKEN"
    
    # Initialize the Updater
    updater = Updater(API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Add the start command handler
    dispatcher.add_handler(CommandHandler("help", help))

    # Add the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start polling to listen for messages
    updater.start_polling()
    print("Bot is running...")
    
    # Keep the bot running until manually stopped
    updater.idle()

# Run the script
if __name__ == "__main__":
    main()
