import bot

Env = bot.Environment()
tg_bot = bot.telebot.TeleBot(token=Env.TG_BOT_TOKEN, parse_mode='Markdown', allow_sending_without_reply=True)

bot_details = tg_bot.get_me()
bot.Bot_Permissions(tg_bot, bot_details)

tg_bot.infinity_polling()