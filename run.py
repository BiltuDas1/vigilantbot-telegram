import bot
import telebot

Env = bot.Environment()
tg_bot = telebot.TeleBot(token=Env.TG_BOT_TOKEN, parse_mode="Markdown")

@tg_bot.message_handler(func=lambda message: True)
def on_message(message):
    msg = tg_bot.copy_message(
        from_chat_id=message.chat.id,
        chat_id=message.chat.id,
        message_id=message.message_id
    )

tg_bot.infinity_polling()