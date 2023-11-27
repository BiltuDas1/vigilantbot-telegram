class Bot_Permissions:
    """
    Checks if bot got enough permissions to operate on group, if it not then leave the group
    """
    def __init__(self, bot, bot_details):
        @bot.message_handler(func=lambda message: True, content_types=('new_chat_members'))
        def check_permission(message):
            for members in message.new_chat_members:
                if members.id == bot_details.id:
                    # Looking for bot name in Administrator
                    for admin in bot.get_chat_administrators(message.chat.id):
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

                            if error_permissions == str():
                                break

                            # Send warning to group
                            bot.send_message(
                                chat_id=message.chat.id,
                                text=f"The bot don't have the following permissions to operate on this group:\n{error_permissions}"
                            )

                            # Leave the group
                            bot.leave_chat(message.chat.id)
                            break
                            # if admin.can_manage_chat and admin.can_delete_messages and admin.can_restrict_members and admin.can_promote_members and admin.can_pin_messages:
                            #     break
                            # else:
                            #     # Send warning to group and leave the group
                            #     bot.send_message(
                            #         chat_id=message.chat.id,
                            #         text="Error: Not Enough Permission"
                            #     )

                            #     bot.leave_chat(message.chat.id)
                            #     break
                    break