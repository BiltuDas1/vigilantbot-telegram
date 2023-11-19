from dotenv import load_dotenv
import os
from . import error

class Environment:
    """
    Loads all the required Environments from the system
    """
    def __init__(self):
        # Loading .env file (If exists)
        load_dotenv()

        # Loading Environments to variables
        self.__load_environ()

        # Verifying
        self.__validate_bot_token()


    def __load_environ(self):
        self.TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
        
    def __validate_bot_token(self):
        if self.TG_BOT_TOKEN is None or len(self.TG_BOT_TOKEN) == 0:
            raise error.Error('NO_TG_BOT_TOKEN')
        
        if self.TG_BOT_TOKEN.find(":") == -1:
            raise error.Error('INVALID_TG_BOT_TOKEN')
        
        if not self.TG_BOT_TOKEN[:self.TG_BOT_TOKEN.find(":")].isdigit():
            raise error.Error('INVALID_TG_BOT_TOKEN')
        
        if not self.TG_BOT_TOKEN[self.TG_BOT_TOKEN.find(":")+1:].isalnum():
            raise error.Error('INVALID_TG_BOT_TOKEN')