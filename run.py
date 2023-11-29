import bot
print("Vigilant bot has been started")

Env = bot.Environment()
tg_bot = bot.telebot.TeleBot(token=Env.TG_BOT_TOKEN, parse_mode='Markdown', allow_sending_without_reply=True)
bot_details = tg_bot.get_me()

@tg_bot.message_handler(func=lambda message: True, content_types=('new_chat_members'))
def check_new_members(message):
    for member in message.new_chat_members:
        # If the bot is joined
        if member.id == bot_details.id:
            # Looking for bot name in Administrator
            for admin in tg_bot.get_chat_administrators(message.chat.id):
                if admin.user.id == bot_details.id:
                    error_permissions = str()
                    if not admin.can_manage_chat:
                        error_permissions += "\ncan\_manage\_chat"
                    if not admin.can_delete_messages:
                        error_permissions += "\ncan\_delete\_messages"
                    if not admin.can_restrict_members:
                        error_permissions += "\ncan\_restrict\_members"
                    if not admin.can_promote_members:
                        error_permissions += "\ncan\_promote\_members"
                    if not admin.can_pin_messages:
                        error_permissions += "\ncan\_pin\_messages"

                    # If the bot is admin and have all the required permissions
                    if error_permissions == str():
                        break

                    # Send warning to group
                    tg_bot.send_message(
                        chat_id=message.chat.id,
                        text=f"The bot don't have the following permissions to operate on this group:\n{error_permissions}"
                    )

                    # Leave the group
                    tg_bot.leave_chat(message.chat.id)
                    break

            else:
                tg_bot.send_message(
                    chat_id=message.chat.id,
                    text="Error: Bot is not an administrator of this group"
                )

                tg_bot.leave_chat(message.chat.id)
                break

        # If the chat member is in the spamwatch list
        if bot.spamwatch.Client(Env.SPAMWATCH_API_KEY).get_ban(member.id):
            tg_bot.restrict_chat_member(permissions=bot.telebot.types.ChatPermissions(
                can_send_messages=False,
                can_send_audios=False,
                can_send_documents=False,
                can_send_photos=False,
                can_send_videos=False,
                can_send_video_notes=False,
                can_send_voice_notes=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False
            ), chat_id=message.chat.id, user_id=member.id)

            if not member.username:
                tg_bot.send_message(
                    chat_id=message.chat.id,
                    text=f"[{member.first_name}](tg://user?id={member.id}) is muted by SpamWatch\nFalse Positive? [Contact SpamWatch](https://t.me/SpamWatchBot)",
                    disable_web_page_preview=True
                )
            else:
                tg_bot.send_message(
                    chat_id=message.chat.id,
                    text=f"@{member.username} is muted by SpamWatch\nFalse Positive? [Contact SpamWatch](https://t.me/SpamWatchBot)",
                    disable_web_page_preview=True
                )

# Nudity image remover
@tg_bot.message_handler(content_types=('photo'))
def check_new_messages(message):
    for photo in message.photo:
        # Getting image url
        file_download_url = tg_bot.get_file_url(photo.file_id)

        # Downloading image
        response, content = bot.httplib2.Http().request(file_download_url, 'GET')

        # Creating directory
        if not bot.os.path.exists(f"temp/{message.chat.id}/images"):
            bot.os.makedirs(f"temp/{message.chat.id}/images")

        # Saving image
        with open(f"temp/{message.chat.id}/images/{photo.file_unique_id}.jpg", 'wb') as f:
            f.write(content)

        # Detecting pornography
        nude_detect = bot.nudenet.NudeDetector().detect(f"temp/{message.chat.id}/images/{photo.file_unique_id}.jpg")

        restricted = (
            "BUTTOCKS_EXPOSED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "ANUS_EXPOSED",
            "MALE_GENITALIA_EXPOSED"
        )

        for data in nude_detect:
            if data['class'] in restricted:
                # Deleting message
                tg_bot.delete_message(
                    chat_id=message.chat.id, 
                    message_id=message.message_id
                )

                # Restricting user
                tg_bot.restrict_chat_member(permissions=bot.telebot.types.ChatPermissions(
                    can_send_messages=False,
                    can_send_audios=False,
                    can_send_documents=False,
                    can_send_photos=False,
                    can_send_videos=False,
                    can_send_video_notes=False,
                    can_send_voice_notes=False,
                    can_send_polls=False,
                    can_send_other_messages=False,
                    can_add_web_page_previews=False
                ), chat_id=message.chat.id, user_id=message.from_user.id)

                # Send a Warning to user, and if it false positive then contact @BiltuDas1
                if message.from_user.username:
                    tg_bot.send_message(
                        chat_id=message.chat.id,
                        text=f"@{message.from_user.username} is muted due to spreading of pornography\nFalse Positive? [Contact Developer](https://t.me/BiltuDas1)"
                    )
                else:
                    tg_bot.send_message(
                        chat_id=message.chat.id,
                        text=f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) is muted due to spreading of pornography\nFalse Positive? [Contact Developer](https://t.me/BiltuDas1)"
                    )
                break
        
        # Deleting image
        bot.os.remove(f"temp/{message.chat.id}/images/{photo.file_unique_id}.jpg")

# Start the bot
tg_bot.infinity_polling()