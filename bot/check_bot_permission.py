class Bot_Permissions:
    """
    Checks if bot got enough permissions to operate on group, if it not then leave the group
    """
    def __init__(self, bot, bot_id):
        @bot.message_handler(func=lambda message: True, content_types=('new_chat_members'))
        def check_permission(message):
            for members in message.new_chat_members:
                if members.id == bot_id.id:
                    # Looking for bot name in Administrator
                    for admin in bot.get_chat_administrators(message.chat.id):
                        if admin.user.id == bot_id.id:
                            if admin.can_manage_chat and admin.can_delete_messages and admin.can_restrict_members and admin.can_promote_members and admin.can_pin_messages:
                                break
                            else:
                                # Send warning to group and leave the group
                                bot.send_message(
                                    chat_id=message.chat.id,
                                    text="Error: Not Enough Permission"
                                )

                                bot.leave_chat(message.chat.id)
                                break
                    break